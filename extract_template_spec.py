#!/usr/bin/env python3
"""
Extract layout specs from Scale .pptx templates for spec-driven generation.

Run this when templates change to regenerate template_spec.json.
The generator uses this spec to match template styling instead of hard-coded values.

Usage:
    python3 extract_template_spec.py
"""
import json
import zipfile
from pathlib import Path

import lxml.etree as ET

NS = {
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}


def emu_to_inches(emu):
    return emu / 914400 if emu is not None else 0


def extract_shapes_from_tree(root, rels_map):
    shapes = []
    for pic in root.findall(".//p:pic", NS):
        cNvPr = pic.find(".//p:nvPicPr/p:cNvPr", NS)
        if cNvPr is None:
            continue
        title = cNvPr.get("title", "")
        name = cNvPr.get("name", "")
        blip = pic.find(".//a:blipFill/a:blip", NS)
        rid = blip.get(f"{{{NS['r']}}}embed") if blip is not None else None
        media_path = rels_map.get(rid, "") if rid else ""
        xfrm = pic.find(".//a:xfrm", NS)
        if xfrm is not None:
            off = xfrm.find("a:off", NS)
            ext = xfrm.find("a:ext", NS)
            if off is not None and ext is not None:
                x = emu_to_inches(int(off.get("x", 0)))
                y = emu_to_inches(int(off.get("y", 0)))
                w = emu_to_inches(int(ext.get("cx", 0)))
                h = emu_to_inches(int(ext.get("cy", 0)))
                shapes.append(
                    {
                        "type": "picture",
                        "title": title,
                        "name": name,
                        "media": media_path.split("/")[-1] if media_path else "",
                        "left": round(x, 3),
                        "top": round(y, 3),
                        "width": round(w, 3),
                        "height": round(h, 3),
                    }
                )
    for sp in root.findall(".//p:sp", NS):
        cNvPr = sp.find(".//p:nvSpPr/p:cNvPr", NS)
        if cNvPr is None:
            continue
        name = cNvPr.get("name", "")
        xfrm = sp.find(".//a:xfrm", NS)
        if xfrm is not None:
            off = xfrm.find("a:off", NS)
            ext = xfrm.find("a:ext", NS)
            if off is not None and ext is not None:
                x = emu_to_inches(int(off.get("x", 0)))
                y = emu_to_inches(int(off.get("y", 0)))
                w = emu_to_inches(int(ext.get("cx", 0)))
                h = emu_to_inches(int(ext.get("cy", 0)))
                shapes.append(
                    {
                        "type": "shape",
                        "name": name,
                        "left": round(x, 3),
                        "top": round(y, 3),
                        "width": round(w, 3),
                        "height": round(h, 3),
                    }
                )
    return shapes


def extract_template(tpl_path, project_root):
    """Extract layout spec from a .pptx template. Uses relative path for portability."""
    try:
        rel_path = tpl_path.relative_to(project_root)
    except ValueError:
        rel_path = tpl_path.name
    spec = {"path": str(rel_path), "slide_width": 10, "slide_height": 5.625}
    with zipfile.ZipFile(tpl_path) as z:
        pres = ET.fromstring(z.read("ppt/presentation.xml"))
        sldSz = pres.find(".//p:sldSz", NS)
        if sldSz is not None:
            spec["slide_width"] = emu_to_inches(int(sldSz.get("cx", 9144000)))
            spec["slide_height"] = emu_to_inches(int(sldSz.get("cy", 5143500)))

        layouts = {}
        for f in z.namelist():
            if "slideLayout" not in f or not f.endswith(".xml"):
                continue
            layout_xml = z.read(f)
            layout_name = Path(f).stem
            rels_path = f.replace(".xml", ".xml.rels").replace(
                "slideLayouts/", "slideLayouts/_rels/"
            )
            rels_map = {}
            if rels_path in z.namelist():
                rels = ET.fromstring(z.read(rels_path))
                for r in rels:
                    if "image" in r.get("Type", "").lower() or "media" in r.get("Target", ""):
                        rels_map[r.get("Id")] = r.get("Target", "")
            root = ET.fromstring(layout_xml)
            shapes = extract_shapes_from_tree(root, rels_map)
            layouts[layout_name] = {"shapes": shapes}

        spec["layouts"] = layouts

        logos = []
        for layout_name, layout_data in layouts.items():
            for s in layout_data["shapes"]:
                if s.get("type") == "picture" and (
                    "logo" in s.get("title", "").lower()
                    or "scale" in s.get("title", "").lower()
                    or "logotype" in s.get("title", "").lower()
                ):
                    logos.append(
                        {
                            "layout": layout_name,
                            "title": s.get("title", ""),
                            "media": s.get("media", ""),
                            "left": s["left"],
                            "top": s["top"],
                            "width": s["width"],
                            "height": s["height"],
                        }
                    )
        spec["logos"] = logos

    return spec


def main():
    project_root = Path(__file__).resolve().parent
    templates_dir = project_root / "templates"
    output_path = project_root / "template_spec.json"

    specs = {}
    for tpl in templates_dir.glob("*.pptx"):
        if tpl.name.startswith("~$"):
            continue
        try:
            spec = extract_template(tpl, project_root)
            specs[tpl.name] = spec
        except Exception as e:
            print(f"Warning: could not extract {tpl.name}: {e}")

    with open(output_path, "w") as f:
        json.dump(specs, f, indent=2)

    print(f"Wrote {output_path}")
    for name, spec in specs.items():
        print(f"  {name}: {len(spec.get('layouts', {}))} layouts, {len(spec.get('logos', []))} logos")


if __name__ == "__main__":
    main()
