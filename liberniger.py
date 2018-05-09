#!/usr/bin/python
#
# What's needed to process everything:
# - use filenames in images folders to produce HTML images_* entries
#       - images 1v-91r
#       - front and back matter
#       - gatherings
#       - external
#       - interleaves
#       - scholars' notes
#       - comparanda (incl. liber niger)
#       - watermarks
# - call image magick to resize images into target sizes
# - convert Introduction with XML to HTML (includes abbreviations)
#       - important are the <link> entries of various types, which must match
#         the generated sections, e.g. images linked via 'f_1r.jpg' but actual
#         file is 1r.jpg
# - convert Introduction Notes in XML Format to HTML
# - convert Peterborough bibliography to HTML
# etc. etc.
#
import os
import subprocess
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
import codecs

def printimgdiv(imgname):
    print('<div id="img_f_' + imgname + '" class="img">')
    print('    <div class="src">' + imgname + '</div>')
    print('    <div class="title">' + imgname + '</div>')
    print('</div>')
    return;

def allimgdiv():
    # generate HTML for all images
    printimgdiv('xiiv')
    for imgno in range(1, 92):
            for side in ('r', 'v'):
                    printimgdiv(str(imgno) + side)
                    continue
            continue
    return

def allimgdivfromdir(src):
    # generate HTML for all images in src - but what about the order?
    os.chdir(src)
    imgs = os.listdir(src)
    for img in imgs:
        printimgdiv(Path(img).stem)
        continue
    return

def allimgdivfromfile(orderfile):
    # generate HTML for all images listed in orderfile
    ofile = open(orderfile, 'r');
    for line in ofile:
        printimgdiv(line.strip())
        continue
    return

def callmagick(src, dest, prefix, imgname, height, dir, format):
    destdir = dest + prefix + '_' + dir
    if not os.path.exists(destdir):
        os.makedirs(destdir)
    cmd = 'magick convert "' + src + imgname + '" -resize x' + str(height) + ' "' + destdir + '/' + Path(imgname).stem + '.' + format + '"'
    print(cmd)
    subprocess.call(cmd)
    return

def allmagick(src, dest, prefix):
    os.chdir(src)
    imgs = os.listdir(src)
    for img in imgs:
        # image magick for each image - produce 360 600 png, 600_gif, 1200 2400 3600 jpg
        callmagick(src, dest, prefix, img, 120, 'thumb', 'gif')
        callmagick(src, dest, prefix, img, 360, '360', 'png')
        callmagick(src, dest, prefix, img, 600, '600', 'png')
        # callmagick(src, dest, prefix, img, 600, '600_gif', 'gif')
        callmagick(src, dest, prefix, img, 1200, '1200', 'jpg')
        callmagick(src, dest, prefix, img, 2400, '2400', 'jpg')
        callmagick(src, dest, prefix, img, 3600, '3600', 'jpg')
        continue
    return

def allmagicklist(src, dest, prefix, listfile):
    lfile = open(listfile, 'r');
    for img in lfile:
        img = img.strip()
        # image magick for each image - produce 360 600 png, 600_gif, 1200 2400 3600 jpg
        callmagick(src, dest, prefix, img, 120, 'thumb', 'gif')
        callmagick(src, dest, prefix, img, 360, '360', 'png')
        callmagick(src, dest, prefix, img, 600, '600', 'png')
        callmagick(src, dest, prefix, img, 600, '600_gif', 'gif')
        callmagick(src, dest, prefix, img, 1200, '1200', 'jpg')
        callmagick(src, dest, prefix, img, 2400, '2400', 'jpg')
        callmagick(src, dest, prefix, img, 3600, '3600', 'jpg')
        continue
    return

def allmagickvarargs(src, dest, prefix, *imgfiles):
    for img in imgfiles:
        # image magick for each image - produce 360 600 png, 600_gif, 1200 2400 3600 jpg
        callmagick(src, dest, prefix, img, 120, 'thumb', 'gif')
        callmagick(src, dest, prefix, img, 360, '360', 'png')
        callmagick(src, dest, prefix, img, 600, '600', 'png')
        callmagick(src, dest, prefix, img, 600, '600_gif', 'gif')
        callmagick(src, dest, prefix, img, 1200, '1200', 'jpg')
        callmagick(src, dest, prefix, img, 2400, '2400', 'jpg')
        callmagick(src, dest, prefix, img, 3600, '3600', 'jpg')
        continue
    return

def allcopyimages(src, dest, srcprefix, destprefix):
    os.chdir(src)
    imgs = os.listdir(src)
    for img in imgs:
        # image magick for each image - produce 360 600 png, 600_gif, 1200 2400 3600 jpg
        callmagick(src, dest, prefix, img, 120, 'thumb', 'gif')
        callmagick(src, dest, prefix, img, 360, '360', 'png')
        callmagick(src, dest, prefix, img, 600, '600', 'png')
        callmagick(src, dest, prefix, img, 600, '600_gif', 'gif')
        callmagick(src, dest, prefix, img, 1200, '1200', 'jpg')
        callmagick(src, dest, prefix, img, 2400, '2400', 'jpg')
        callmagick(src, dest, prefix, img, 3600, '3600', 'jpg')
        continue
    return

def alllinkstoas(infile, outfile):
    reerr = re.compile(r"<link type=\"nt\" id=\"nx_([a-z_0-9]*?)\" ref=\"nt_[a-z_0-9 \-]*?\">\*</link>")
    renti = re.compile(r"<link type=\"nt\" id=\"nxi_([a-z_0-9]*?)\" ref=\"nti_[a-z_0-9 \-]*?\">\*</link>")
    reann = re.compile(r"<link id=\"annal_([0-9A-Za-z\._]*?)\" (trans=\".*?\")>(.*?)</link>")
    reimg = re.compile(r"<folio id=\"f([A-Za-z0-9]*?)\" ref=\"f_([_A-Za-z0-9\.]*?)\" title=\"f. ([_A-Za-z0-9\.]*?)\"/>")
    regen = re.compile(r"<link type=\"([a-z ]*?)\" ref=\"[a-z]*?_([_a-zA-Z0-9]*?)\">(.*?)</link>")

    # rebib = re.compile(r"<link type=\"bib\" ref=\"bib_([A-Za-z0-9\.]*?)\">(.*?)</link>")
    # reann = re.compile(r"<link type=\"annal\" ref=\"annal_([0-9A-Za-z\._]*?)\">(.*?)</link>")
    # rewit = re.compile(r"<link type=\"wit\" ref=\"wit_([A-Za-z0-9]*?)\">(.*?)</link>")
    # reimg = re.compile(r"<link type=\"img\" ref=\"([_A-Za-z0-9\.]*?)\">(.*?)</link>")
    # reabb = re.compile(r"<link type=\"abbr\" ref=\"abbr_([_A-Za-z0-9]*?)\">(.*?)</link>")
    # reint = re.compile(r"<link type=\"intro\" ref=\"intro_([_0-9]*?)\">(.*?)</link>")
    # rewtn = re.compile(r"<note id=\"wit_([a-zA-Z0-9]*?)\" type=\"wit\">")
    
    introfile = open(infile, 'r');
    destfile = open(outfile, 'w') 
    for line in introfile:
        # correct errors
        line = line.replace("=\" ", "=\"")
        line = line.replace("_ ", "_")
        line = line.replace(" _", "_")
        line = line.replace(" \">", "\">")
        # process
        line = reerr.sub("<a id=\"nx_\\1\" href=\"nt_\\1\" class=\"link nt\">*</a>", line)
        line = renti.sub("<a id=\"nxi_\\1\" href=\"nti_\\1\" class=\"link nt\">*</a>", line)
        line = reann.sub("<a href=\"annal_\\1\" class=\"link annal\" \\2>\\3</a>", line)
        line = reimg.sub("<a href=\"f_\\1\" class=\"link img\">f. \\3</a>", line)
        line = regen.sub("<a href=\"\\1_\\2\" class=\"link \\1\">\\3</a>", line)
        # match = regen.search(line)
        # if (match):
            # type = match.group(1).strip()
            # ref = match.group(2).strip()
            # text = match.group(3)
            # newlink = "<a href=\"" + type + "_" + ref + "\" class=\"link " + type + "\">" + text + "</a>"
            # line = regen.sub(newlink, line)
            # continue

        # line = rebib.sub("<a href=\"bib_\\1\" class=\"link bib\">\\2</a>", line)
        # line = rewit.sub("<a href=\"wit_\\1\" class=\"link wit\">\\2</a>", line)
        # line = reabb.sub("<a href=\"abbr_\\1\" class=\"link abbr\">\\2</a>", line)
        # line = reint.sub("<a href=\"intro_\\1\" class=\"link intro\">\\2</a>", line)

        line = line.replace("<blockquote>", "<div class=\"blockquote\">")
        line = line.replace("</blockquote>", "</div>")
        
        # line = line.replace("<notes id=\"notes_witness\" type=\"note_witness\">", "<div id=\"notes_witness\" class=\"notes note_witness\">")
        # line = line.replace("</notes>", "</div>")
        # line = rewtn.sub("<div id=\"wit_\\1\" class=\"note wit\">", line)
        # line = line.replace("<title>", "<div class=\"title\">")
        # line = line.replace("</title>", "</div>")
        # line = line.replace("<desc>", "<div class=\"desc\">")
        # line = line.replace("</desc>", "</div>")
        # line = line.replace("</note>", "</div>")
        
#        needed correction:
#           href=\"f_(.*?)\.jpg\" class=\"link img\" -> href="f_$1" class="link img"    
#           " & " -> " &amp; "
#           "< link" -> "<link"
#           added <!ENTITY dagger "&#8224;" >
#           ([^<])/([a-z_]+?)> -> $1</$2>
#           map-notes missing "in at end of <link
        destfile.write(line) 
        # sys.stdout.write(line)
        continue
    introfile.close()
    destfile.close()
    return

def processxmltext(textfile):
    tree = ET.parse(textfile)
    root = tree.getroot()
    root.findall('section_title')
    for child in root:
        print(child.tag, child.attrib)
    return
 
def processhmms(srcdir):
    # <area shape=\"rect\" coords=\"260,3552,661,3688\" href=\"nt_1r_26\">
    remap = re.compile(r"<area shape=\\\"rect\\\" coords=\\\"([0-9\-]*),([0-9\-]*),([0-9\-]*),([0-9\-]*)\\\" href=\\\"n[tx]_([a-z0-9_]*)\\\">")
    os.chdir(srcdir)
    hmms = os.listdir(srcdir)
    for hmm in hmms:
        if hmm.endswith(".hmm"):
            page = Path(hmm).stem[2:].lstrip('0')
            hmmfile = open(hmm, 'r');
            print('<div id="map_' + page + '" class="map">')
            for line in hmmfile:
                if "<area shape" in line:
                    line = remap.sub('<div id="mx_\\5" class="rect">\\1 \\2 \\3 \\4</div>', line)
                    if not "<area " in line:
                        sys.stdout.write(line)
                        continue
                    continue
                continue
            print('</div>')
            continue
        continue
    return

def addbeowulfimglinks(textsrc, transdest):
    relnk = re.compile(r"link img\">(.*?)</a></span></td><td><span id=\"(.*?)a\">")
        
    with codecs.open(transdest, 'r', 'utf-8') as content_file:
        content = content_file.read().strip()
    textfile = codecs.open(textsrc, 'r', 'utf-8')
    output = " "
    for line in textfile:
        if "link img\">" in line:
            match = relnk.search(line)
            if (match):
                folio = match.group(1)
                lineno = match.group(2)
                relno = re.compile(r'^' + lineno + '\.', re.MULTILINE)
                transfile = codecs.open(transdest, 'r', 'utf-8')
                #for tline in transfile:
                content = relno.sub("<a href=\"f_" + str(folio) + "\" class=\"link img\">" + str(folio) + "</a>&nbsp;\r\n" + str(lineno) + ".", content)
                #    continue
                continue
            continue
        continue
    sys.stdout.write(content)
    return
    
# main thread...
#
#allimgdiv()
#allnotesintro("E:/Downloads/Evellum/peterborough_master/map-notes.xml")
#processxmltext("E:/Downloads/Evellum/peterborough_master/introwithxml.xml")
#processhmms("E:/Downloads/Evellum/peterborough_master/hotspot mapping")
#allmagick('E:/Downloads/Evellum/exeter/bigimages/exeter3500/',
#        'E:/Downloads/Evellum/exeter3.0/resources/facsimiles/Ex_Cath_Lib_MS_3501/',
#        'exeter')
#allmagicklist('E:/Downloads/evellum.com/beowulf/resources/facsimiles/Cot_Vit_A_xv/beowulf_originals/',
#        'E:/Downloads/evellum.com/beowulf/resources/facsimiles/Cot_Vit_A_xv/',
#       'beowulf',
#       'E:/Downloads/Evellum/asce_master/missing.txt')
#allmagickvarargs('E:/Downloads/evellum.com/beowulf/resources/facsimiles/Cot_Vit_A_xv/beowulf_originals/',
#        'E:/Downloads/evellum.com/beowulf/resources/facsimiles/Cot_Vit_A_xv/',
#       'beowulf',
#       '134v.jpg')
#allimgdivfromfile('E:/Downloads/Evellum/peterborough_master/junius-order.txt')
#allimgdivfromdir('E:/Downloads/beowulf/resources/facsimiles/Cot_Vit_A_xv/beowulf_originals/')
#addbeowulfimglinks('E:/Downloads/evellum.com/beowulf/engine/beowulf.text.html', 'E:/Downloads/evellum.com/beowulf/engine/beowulf.trans.html')
#alllinkstoas("E:/Downloads/Evellum/asce_master/ASC Text.xml", "E:/Downloads/Evellum/asce_master/asce-text.html")
#alllinkstoas("E:/Downloads/Evellum/asce_master/ASC Trans.xml", "E:/Downloads/Evellum/asce_master/asce-trans.html")
#allimgdivfromdir('E:/Downloads/Evellum/asce_master/images/liber niger/')
allmagick('E:/Downloads/Evellum/asce_master/images/liber niger/',
        'E:/Downloads/evellum.com/asce/resources/facsimiles/liberniger/',
        'liberniger')
