%global tl_version 2018
%global _texdir %{_datadir}/texlive
%global __brp_mangle_shebangs /usr/bin/true

Name:           texlive-split-u
Version:        %{tl_version}
Release:        24
Epoch:          8
Summary:        TeX formatting system
License:        Artistic 2.0 and GPLv2 and GPLv2+ and LGPLv2+ and LPPL and MIT and Public Domain and UCD and Utopia
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0003:     texlive-licenses.tar.xz
Source1507:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rsc.tar.xz
Source1508:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rsc.doc.tar.xz
Source2039:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/roboto.tar.xz
Source2040:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/roboto.doc.tar.xz
Source2041:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/romande.tar.xz
Source2042:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/romande.doc.tar.xz
Source2044:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rsfso.tar.xz
Source2045:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rsfso.doc.tar.xz
Source2046:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sansmathaccent.tar.xz
Source2047:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sansmathaccent.doc.tar.xz
Source2048:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sansmathfonts.tar.xz
Source2049:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sansmathfonts.doc.tar.xz
Source2050:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sauter.tar.xz
Source2051:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sauterfonts.tar.xz
Source2052:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sauterfonts.doc.tar.xz
Source2054:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/schulschriften.tar.xz
Source2055:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/schulschriften.doc.tar.xz
Source2056:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/semaphor.tar.xz
Source2057:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/semaphor.doc.tar.xz
Source2142:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rsfs.tar.xz
Source2143:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rsfs.doc.tar.xz
Source2245:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/schwalbe-chess.tar.xz
Source2246:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/schwalbe-chess.doc.tar.xz
Source2248:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sgame.tar.xz
Source2249:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sgame.doc.tar.xz
Source2321:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/schemata.tar.xz
Source2322:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/schemata.doc.tar.xz
Source2458:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rrgtrees.tar.xz
Source2459:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rrgtrees.doc.tar.xz
Source2461:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rtklage.tar.xz
Source2462:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rtklage.doc.tar.xz
Source2463:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/screenplay.tar.xz
Source2464:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/screenplay.doc.tar.xz
Source2466:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/screenplay-pkg.tar.xz
Source2467:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/screenplay-pkg.doc.tar.xz
Source2556:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ruhyphen.tar.xz
Source2581:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/serbian-apostrophe.tar.xz
Source2582:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/serbian-apostrophe.doc.tar.xz
Source2583:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/serbian-date-lat.tar.xz
Source2584:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/serbian-date-lat.doc.tar.xz
Source2585:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/serbian-def-cyr.tar.xz
Source2586:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/serbian-def-cyr.doc.tar.xz
Source2587:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/serbian-lig.tar.xz
Source2588:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/serbian-lig.doc.tar.xz
Source2776:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/r_und_s.tar.xz
Source2777:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/r_und_s.doc.tar.xz
Source2839:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sanskrit.tar.xz
Source2840:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sanskrit.doc.tar.xz
Source2842:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sanskrit-t1.tar.xz
Source2843:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sanskrit-t1.doc.tar.xz
Source3085:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sansmath.tar.xz
Source3086:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sansmath.doc.tar.xz
Source3087:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/section.tar.xz
Source3088:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/section.doc.tar.xz
Source3089:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/seminar.tar.xz
Source3090:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/seminar.doc.tar.xz
Source3091:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sepnum.tar.xz
Source3092:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sepnum.doc.tar.xz
Source3093:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/setspace.tar.xz
Source3094:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/setspace.doc.tar.xz
Source3273:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rviewport.tar.xz
Source3274:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rviewport.doc.tar.xz
Source3276:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sa-tikz.tar.xz
Source3277:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sa-tikz.doc.tar.xz
Source3278:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/schemabloc.tar.xz
Source3279:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/schemabloc.doc.tar.xz
Source3280:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/setdeck.tar.xz
Source3281:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/setdeck.doc.tar.xz
Source3378:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sauerj.tar.xz
Source3379:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sauerj.doc.tar.xz
Source5113:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/robustcommand.tar.xz
Source5114:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/robustcommand.doc.tar.xz
Source5116:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/robustindex.tar.xz
Source5117:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/robustindex.doc.tar.xz
Source5118:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/romanbar.tar.xz
Source5119:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/romanbar.doc.tar.xz
Source5121:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/romanbarpagenumber.tar.xz
Source5122:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/romanbarpagenumber.doc.tar.xz
Source5124:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/romanneg.tar.xz
Source5125:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/romanneg.doc.tar.xz
Source5126:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/romannum.tar.xz
Source5127:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/romannum.doc.tar.xz
Source5129:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rotfloat.tar.xz
Source5130:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rotfloat.doc.tar.xz
Source5132:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rotpages.tar.xz
Source5133:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rotpages.doc.tar.xz
Source5134:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/roundbox.tar.xz
Source5135:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/roundbox.doc.tar.xz
Source5136:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rterface.tar.xz
Source5137:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rterface.doc.tar.xz
Source5138:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rtkinenc.tar.xz
Source5139:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rtkinenc.doc.tar.xz
Source5141:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rulercompass.tar.xz
Source5142:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rulercompass.doc.tar.xz
Source5144:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rvwrite.tar.xz
Source5145:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rvwrite.doc.tar.xz
Source5146:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/savefnmark.tar.xz
Source5147:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/savefnmark.doc.tar.xz
Source5149:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/savesym.tar.xz
Source5150:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/savetrees.tar.xz
Source5151:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/savetrees.doc.tar.xz
Source5153:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/scale.tar.xz
Source5154:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/scale.doc.tar.xz
Source5156:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/scalebar.tar.xz
Source5157:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/scalebar.doc.tar.xz
Source5159:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/scalerel.tar.xz
Source5160:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/scalerel.doc.tar.xz
Source5161:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/scanpages.tar.xz
Source5162:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/scanpages.doc.tar.xz
Source5163:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sdrt.tar.xz
Source5164:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sdrt.doc.tar.xz
Source5165:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/secdot.tar.xz
Source5166:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/secdot.doc.tar.xz
Source5167:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sectionbox.tar.xz
Source5168:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sectionbox.doc.tar.xz
Source5169:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sectsty.tar.xz
Source5170:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sectsty.doc.tar.xz
Source5172:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/seealso.tar.xz
Source5173:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/seealso.doc.tar.xz
Source5175:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/selectp.tar.xz
Source5176:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/selectp.doc.tar.xz
Source5177:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/semantic.tar.xz
Source5178:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/semantic.doc.tar.xz
Source5180:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/semioneside.tar.xz
Source5181:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/semioneside.doc.tar.xz
Source5183:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/semproc.tar.xz
Source5184:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/semproc.doc.tar.xz
Source5186:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sepfootnotes.tar.xz
Source5187:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sepfootnotes.doc.tar.xz
Source5188:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/seqsplit.tar.xz
Source5189:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/seqsplit.doc.tar.xz
Source5191:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sf298.tar.xz
Source5192:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sf298.doc.tar.xz
Source5194:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sffms.tar.xz
Source5195:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sffms.doc.tar.xz
Source5197:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sfmath.tar.xz
Source5815:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/selnolig.tar.xz
Source5816:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/selnolig.doc.tar.xz
Source5898:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sesamanuel.tar.xz
Source5899:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sesamanuel.doc.tar.xz
Source6005:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/roex.tar.xz
Source6007:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/roundrect.tar.xz
Source6008:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/roundrect.doc.tar.xz
Source6505:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ryethesis.tar.xz
Source6506:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ryethesis.doc.tar.xz
Source6508:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sageep.tar.xz
Source6509:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sageep.doc.tar.xz
Source6511:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sapthesis.tar.xz
Source6512:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sapthesis.doc.tar.xz
Source6513:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/scrjrnl.tar.xz
Source6514:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/scrjrnl.doc.tar.xz
Source6516:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/schule.tar.xz
Source6517:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/schule.doc.tar.xz
Source6519:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sduthesis.tar.xz
Source6520:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sduthesis.doc.tar.xz
Source6522:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/seuthesis.tar.xz
Source6523:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/seuthesis.doc.tar.xz
Source6713:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sasnrdisplay.tar.xz
Source6714:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sasnrdisplay.doc.tar.xz
Source6715:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sciposter.tar.xz
Source6716:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sciposter.doc.tar.xz
Source6717:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sclang-prettifier.tar.xz
Source6718:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sclang-prettifier.doc.tar.xz
Source6720:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sfg.tar.xz
Source6721:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sfg.doc.tar.xz
Source7207:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/scheme-basic.tar.xz
Source7208:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/scheme-context.tar.xz
Source7209:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/scheme-full.tar.xz
Source7210:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/scheme-gust.tar.xz
Source7211:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/scheme-medium.tar.xz
Source7212:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/scheme-minimal.tar.xz
Source7213:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/scheme-small.tar.xz
Source7214:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/scheme-tetex.tar.xz
Source7493:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rosario.tar.xz
Source7494:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rosario.doc.tar.xz
Source7496:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/russ.tar.xz
Source7497:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/russ.doc.tar.xz
Source7498:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sanitize-umlaut.tar.xz
Source7499:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sanitize-umlaut.doc.tar.xz
Source7500:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/scrlttr2copy.tar.xz
Source7501:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/scrlttr2copy.doc.tar.xz
Source7502:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/seuthesix.tar.xz
Source7503:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/seuthesix.doc.tar.xz
Source7937:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rutitlepage.tar.xz
Source7938:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rutitlepage.doc.tar.xz
Source7939:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/scsnowman.tar.xz
Source7940:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/scsnowman.doc.tar.xz
Source7941:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/scratch.tar.xz
Source7942:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/scratch.doc.tar.xz
Source7943:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sesstime.tar.xz
Source7944:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sesstime.doc.tar.xz
Source8300:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/scientific-thesis-cover.tar.xz
Source8301:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/scientific-thesis-cover.doc.tar.xz
Source8302:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/scratchx.tar.xz
Source8303:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/scratchx.doc.tar.xz
Source8304:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sectionbreak.tar.xz
Source8305:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sectionbreak.doc.tar.xz
Source8306:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/semantic-markup.tar.xz
Source8307:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/semantic-markup.doc.tar.xz
Source8308:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sexam.tar.xz
Source8309:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sexam.doc.tar.xz

%description
The TeX Live software distribution offers a complete TeX system for a
variety of Unix, Macintosh, Windows and other platforms. It
encompasses programs for editing, typesetting, previewing and printing
of TeX documents in many different languages, and a large collection
of TeX macros and font libraries.

The distribution includes extensive general documentation about TeX,
as well as the documentation for the included software packages.

%package -n texlive-rsc
Provides:       tex-rsc = %{tl_version}
License:        GPL+
Summary:        BibTeX style for use with RSC journals
Version:        svn41923
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(kvoptions.sty), tex(natbib.sty), tex(natmove.sty), tex(mciteplus.sty)
Provides:       tex(rsc.sty) = %{tl_version}

%description -n texlive-rsc
The rsc package provides a BibTeX style in accordance with the
requirements of the Royal Society of Chemistry. It was
originally based on the file pccp.bst, but also implements a
number of styles from the achemso package. The package is now a
stub for the chemstyle package, which the author developed to
unify the writing of articles with a chemistry content.

%package -n texlive-rsc-doc
Summary:        Documentation for rsc
Version:        svn41923
Provides:       tex-rsc-doc
AutoReqProv:    No

%description -n texlive-rsc-doc
Documentation for rsc

%package -n texlive-roboto
Provides:       tex-roboto = %{tl_version}
License:        ASL 2.0
Summary:        Support for the Roboto family of fonts
Version:        svn47586
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex, tex(ifxetex.sty)
Requires:       tex(ifluatex.sty), tex(xkeyval.sty), tex(textcomp.sty), tex(fontspec.sty)
Requires:       tex(fontenc.sty), tex(fontaxes.sty), tex(mweights.sty)
Provides:       tex(rbto_2gjoqz.enc) = %{tl_version}, tex(rbto_4cxnmx.enc) = %{tl_version}
Provides:       tex(rbto_4j5rgv.enc) = %{tl_version}, tex(rbto_5au2tj.enc) = %{tl_version}
Provides:       tex(rbto_5xgh2b.enc) = %{tl_version}, tex(rbto_a5nkuh.enc) = %{tl_version}
Provides:       tex(rbto_b3vvq3.enc) = %{tl_version}, tex(rbto_bergpl.enc) = %{tl_version}
Provides:       tex(rbto_brv6l3.enc) = %{tl_version}, tex(rbto_bztncd.enc) = %{tl_version}
Provides:       tex(rbto_ddkove.enc) = %{tl_version}, tex(rbto_ebhzxa.enc) = %{tl_version}
Provides:       tex(rbto_h3wntv.enc) = %{tl_version}, tex(rbto_hhyavc.enc) = %{tl_version}
Provides:       tex(rbto_i2gjg4.enc) = %{tl_version}, tex(rbto_idpkzy.enc) = %{tl_version}
Provides:       tex(rbto_ihpqsf.enc) = %{tl_version}, tex(rbto_lxpby6.enc) = %{tl_version}
Provides:       tex(rbto_n6nas2.enc) = %{tl_version}, tex(rbto_oa6oe5.enc) = %{tl_version}
Provides:       tex(rbto_pjd75x.enc) = %{tl_version}, tex(rbto_r7ss7u.enc) = %{tl_version}
Provides:       tex(rbto_rehtu3.enc) = %{tl_version}, tex(rbto_s7kfgd.enc) = %{tl_version}
Provides:       tex(rbto_schjax.enc) = %{tl_version}, tex(rbto_svcybe.enc) = %{tl_version}
Provides:       tex(rbto_t2643k.enc) = %{tl_version}, tex(rbto_tr5a5v.enc) = %{tl_version}
Provides:       tex(rbto_uf77so.enc) = %{tl_version}, tex(rbto_usdwn6.enc) = %{tl_version}
Provides:       tex(rbto_v5svcm.enc) = %{tl_version}, tex(rbto_wkn3wn.enc) = %{tl_version}
Provides:       tex(rbto_yzgzr5.enc) = %{tl_version}, tex(roboto.map) = %{tl_version}
Provides:       tex(Roboto-Black-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-lf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-osf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Black-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-lf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-osf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Bold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-lf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-osf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Italic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-lf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-osf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Light-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-LightItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-lf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-osf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Medium-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-lf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-osf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Regular-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-lf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-osf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-Thin-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-lf-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-osf-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-osf-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-osf-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-osf-ts1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-lf-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-osf-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-lf-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-lf-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-lf-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-lf-ts1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-osf-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-osf-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-osf-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-osf-ts1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-tlf-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-tosf-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-lf-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-lf-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-lf-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-lf-ts1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-osf-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-osf-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-osf-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-osf-ts1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-tosf-t1.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(RobotoSlab-Bold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoSlab-Bold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoSlab-Bold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoSlab-Bold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoSlab-Bold-lf-t1.tfm) = %{tl_version}
Provides:       tex(RobotoSlab-Bold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(RobotoSlab-Bold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(RobotoSlab-Light-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoSlab-Light-lf-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoSlab-Light-lf-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoSlab-Light-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoSlab-Light-lf-t1.tfm) = %{tl_version}
Provides:       tex(RobotoSlab-Light-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(RobotoSlab-Light-lf-ts1.tfm) = %{tl_version}
Provides:       tex(RobotoSlab-Regular-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoSlab-Regular-lf-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoSlab-Regular-lf-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoSlab-Regular-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoSlab-Regular-lf-t1.tfm) = %{tl_version}
Provides:       tex(RobotoSlab-Regular-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(RobotoSlab-Regular-lf-ts1.tfm) = %{tl_version}
Provides:       tex(RobotoSlab-Thin-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(RobotoSlab-Thin-lf-ly1.tfm) = %{tl_version}
Provides:       tex(RobotoSlab-Thin-lf-ot1.tfm) = %{tl_version}
Provides:       tex(RobotoSlab-Thin-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(RobotoSlab-Thin-lf-t1.tfm) = %{tl_version}
Provides:       tex(RobotoSlab-Thin-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(RobotoSlab-Thin-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Roboto-Black.ttf) = %{tl_version}, tex(Roboto-BlackItalic.ttf) = %{tl_version}
Provides:       tex(Roboto-Bold.ttf) = %{tl_version}, tex(Roboto-BoldItalic.ttf) = %{tl_version}
Provides:       tex(Roboto-Light.ttf) = %{tl_version}, tex(Roboto-LightItalic.ttf) = %{tl_version}
Provides:       tex(Roboto-Medium.ttf) = %{tl_version}, tex(Roboto-MediumItalic.ttf) = %{tl_version}
Provides:       tex(Roboto-Regular.ttf) = %{tl_version}, tex(Roboto-RegularItalic.ttf) = %{tl_version}
Provides:       tex(Roboto-Thin.ttf) = %{tl_version}, tex(Roboto-ThinItalic.ttf) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold.ttf) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic.ttf) = %{tl_version}
Provides:       tex(RobotoCondensed-Light.ttf) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic.ttf) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular.ttf) = %{tl_version}
Provides:       tex(RobotoCondensed-RegularItalic.ttf) = %{tl_version}
Provides:       tex(RobotoSlab-Bold.ttf) = %{tl_version}
Provides:       tex(RobotoSlab-Light.ttf) = %{tl_version}
Provides:       tex(RobotoSlab-Regular.ttf) = %{tl_version}
Provides:       tex(RobotoSlab-Thin.ttf) = %{tl_version}
Provides:       tex(Roboto-Black.pfb) = %{tl_version}, tex(Roboto-BlackItalic.pfb) = %{tl_version}
Provides:       tex(Roboto-Bold.pfb) = %{tl_version}, tex(Roboto-BoldItalic.pfb) = %{tl_version}
Provides:       tex(Roboto-Italic.pfb) = %{tl_version}, tex(Roboto-Light.pfb) = %{tl_version}
Provides:       tex(Roboto-LightItalic.pfb) = %{tl_version}
Provides:       tex(Roboto-Medium.pfb) = %{tl_version}, tex(Roboto-MediumItalic.pfb) = %{tl_version}
Provides:       tex(Roboto-Regular.pfb) = %{tl_version}, tex(Roboto-Thin.pfb) = %{tl_version}
Provides:       tex(Roboto-ThinItalic.pfb) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold.pfb) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic.pfb) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic.pfb) = %{tl_version}
Provides:       tex(RobotoCondensed-Light.pfb) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic.pfb) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular.pfb) = %{tl_version}
Provides:       tex(RobotoSlab-Bold.pfb) = %{tl_version}
Provides:       tex(RobotoSlab-Light.pfb) = %{tl_version}
Provides:       tex(RobotoSlab-Regular.pfb) = %{tl_version}
Provides:       tex(RobotoSlab-Thin.pfb) = %{tl_version}
Provides:       tex(Roboto-Black-lf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Black-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Black-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-Black-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Black-lf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Black-lf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-Black-osf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Black-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Black-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-Black-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Black-osf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Black-osf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-Black-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Black-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Black-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-Black-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Black-tlf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Black-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-Black-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Black-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Black-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-Black-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Black-tosf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Black-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-BlackItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-Bold-lf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Bold-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Bold-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-Bold-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Bold-lf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Bold-lf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-Bold-osf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Bold-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Bold-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-Bold-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Bold-osf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Bold-osf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Bold-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Bold-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-Bold-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-Bold-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Bold-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Bold-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-Bold-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Bold-tosf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Bold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-BoldItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-Italic-lf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Italic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Italic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-Italic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Italic-lf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Italic-lf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-Italic-osf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Italic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Italic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-Italic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Italic-osf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Italic-osf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-Italic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Italic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Italic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-Italic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-Italic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Italic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Italic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-Italic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Italic-tosf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Italic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-Light-lf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Light-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Light-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-Light-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Light-lf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Light-lf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-Light-osf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Light-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Light-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-Light-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Light-osf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Light-osf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-Light-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Light-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Light-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-Light-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Light-tlf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Light-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-Light-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Light-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Light-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-Light-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Light-tosf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Light-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-LightItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-LightItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-LightItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-LightItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-LightItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-LightItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-LightItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-LightItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-LightItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-LightItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-LightItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-LightItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-LightItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-LightItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-LightItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-LightItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-LightItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-LightItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-LightItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-LightItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-LightItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-LightItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-LightItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-LightItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-Medium-lf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Medium-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Medium-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-Medium-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Medium-lf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Medium-lf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-Medium-osf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Medium-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Medium-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-Medium-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Medium-osf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Medium-osf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-Medium-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Medium-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Medium-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-Medium-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Medium-tlf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Medium-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-Medium-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Medium-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Medium-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-Medium-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Medium-tosf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Medium-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-MediumItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-Regular-lf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Regular-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Regular-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-Regular-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Regular-lf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Regular-lf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-Regular-osf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Regular-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Regular-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-Regular-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Regular-osf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Regular-osf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-Regular-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Regular-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Regular-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-Regular-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Regular-tlf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Regular-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-Regular-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Regular-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Regular-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-Regular-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Regular-tosf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Regular-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-Thin-lf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Thin-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Thin-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-Thin-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Thin-lf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Thin-lf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-Thin-osf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Thin-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Thin-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-Thin-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Thin-osf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Thin-osf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-Thin-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Thin-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Thin-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-Thin-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Thin-tlf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Thin-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-Thin-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Thin-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-Thin-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-Thin-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Thin-tosf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-Thin-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(Roboto-ThinItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-lf-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-lf-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-lf-ts1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-osf-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-osf-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-osf-ts1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-tosf-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-tosf-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Bold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-BoldItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-lf-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-lf-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-lf-ts1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-osf-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-osf-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-osf-ts1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-tosf-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Italic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-lf-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-lf-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-lf-ts1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-osf-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-osf-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-osf-ts1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-tlf-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-tlf-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-tlf-ts1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-tosf-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-tosf-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Light-tosf-ts1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-LightItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-lf-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-lf-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-lf-ts1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-osf-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-osf-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-osf-ts1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-tlf-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-tlf-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-tlf-ts1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-tosf-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-tosf-t1.vf) = %{tl_version}
Provides:       tex(RobotoCondensed-Regular-tosf-ts1.vf) = %{tl_version}
Provides:       tex(RobotoSlab-Bold-lf-ly1.vf) = %{tl_version}
Provides:       tex(RobotoSlab-Bold-lf-t1.vf) = %{tl_version}
Provides:       tex(RobotoSlab-Bold-lf-ts1.vf) = %{tl_version}
Provides:       tex(RobotoSlab-Light-lf-ly1.vf) = %{tl_version}
Provides:       tex(RobotoSlab-Light-lf-t1.vf) = %{tl_version}
Provides:       tex(RobotoSlab-Light-lf-ts1.vf) = %{tl_version}
Provides:       tex(RobotoSlab-Regular-lf-ly1.vf) = %{tl_version}
Provides:       tex(RobotoSlab-Regular-lf-t1.vf) = %{tl_version}
Provides:       tex(RobotoSlab-Regular-lf-ts1.vf) = %{tl_version}
Provides:       tex(RobotoSlab-Thin-lf-ly1.vf) = %{tl_version}
Provides:       tex(RobotoSlab-Thin-lf-t1.vf) = %{tl_version}
Provides:       tex(RobotoSlab-Thin-lf-ts1.vf) = %{tl_version}
Provides:       tex(LY1Roboto-LF.fd) = %{tl_version}, tex(LY1Roboto-OsF.fd) = %{tl_version}
Provides:       tex(LY1Roboto-TLF.fd) = %{tl_version}, tex(LY1Roboto-TOsF.fd) = %{tl_version}
Provides:       tex(LY1RobotoCondensed-LF.fd) = %{tl_version}
Provides:       tex(LY1RobotoCondensed-OsF.fd) = %{tl_version}
Provides:       tex(LY1RobotoCondensed-TLF.fd) = %{tl_version}
Provides:       tex(LY1RobotoCondensed-TOsF.fd) = %{tl_version}
Provides:       tex(LY1RobotoSlab-LF.fd) = %{tl_version}
Provides:       tex(OT1Roboto-LF.fd) = %{tl_version}, tex(OT1Roboto-OsF.fd) = %{tl_version}
Provides:       tex(OT1Roboto-TLF.fd) = %{tl_version}, tex(OT1Roboto-TOsF.fd) = %{tl_version}
Provides:       tex(OT1RobotoCondensed-LF.fd) = %{tl_version}
Provides:       tex(OT1RobotoCondensed-OsF.fd) = %{tl_version}
Provides:       tex(OT1RobotoCondensed-TLF.fd) = %{tl_version}
Provides:       tex(OT1RobotoCondensed-TOsF.fd) = %{tl_version}
Provides:       tex(OT1RobotoSlab-LF.fd) = %{tl_version}
Provides:       tex(T1Roboto-LF.fd) = %{tl_version}, tex(T1Roboto-OsF.fd) = %{tl_version}
Provides:       tex(T1Roboto-TLF.fd) = %{tl_version}, tex(T1Roboto-TOsF.fd) = %{tl_version}
Provides:       tex(T1RobotoCondensed-LF.fd) = %{tl_version}
Provides:       tex(T1RobotoCondensed-OsF.fd) = %{tl_version}
Provides:       tex(T1RobotoCondensed-TLF.fd) = %{tl_version}
Provides:       tex(T1RobotoCondensed-TOsF.fd) = %{tl_version}
Provides:       tex(T1RobotoSlab-LF.fd) = %{tl_version}, tex(TS1Roboto-LF.fd) = %{tl_version}
Provides:       tex(TS1Roboto-OsF.fd) = %{tl_version}, tex(TS1Roboto-TLF.fd) = %{tl_version}
Provides:       tex(TS1Roboto-TOsF.fd) = %{tl_version}, tex(TS1RobotoCondensed-LF.fd) = %{tl_version}
Provides:       tex(TS1RobotoCondensed-OsF.fd) = %{tl_version}
Provides:       tex(TS1RobotoCondensed-TLF.fd) = %{tl_version}
Provides:       tex(TS1RobotoCondensed-TOsF.fd) = %{tl_version}
Provides:       tex(TS1RobotoSlab-LF.fd) = %{tl_version}
Provides:       tex(roboto.sty) = %{tl_version}

%description -n texlive-roboto
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the Roboto, RobotoCondensed and RobotoSlab families
of fonts, designed by Christian Robertson for Google.

%package -n texlive-roboto-doc
Summary:        Documentation for roboto
Version:        svn47586
Provides:       tex-roboto-doc
AutoReqProv:    No

%description -n texlive-roboto-doc
Documentation for roboto

%package -n texlive-romande
Provides:       tex-romande = %{tl_version}
License:        LPPL
Summary:        Romande ADF fonts and LaTeX support
Version:        svn19537.1.008_v7_sc

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(xkeyval.sty), tex(fontenc.sty), tex(textcomp.sty), tex(nfssext-cfr.sty)
Provides:       tex(romande-supp.enc) = %{tl_version}, tex(t1-romandeadf-alt.enc) = %{tl_version}
Provides:       tex(t1-romandeadf.enc) = %{tl_version}, tex(ts1-euro-yrd.enc) = %{tl_version}
Provides:       tex(yrd.map) = %{tl_version}, tex(s-yrdd.tfm) = %{tl_version}
Provides:       tex(s-yrddi.tfm) = %{tl_version}, tex(s-yrdr.tfm) = %{tl_version}
Provides:       tex(s-yrdri.tfm) = %{tl_version}, tex(s-yrdriw.tfm) = %{tl_version}
Provides:       tex(t1-romandeadf-alt-yrdd.tfm) = %{tl_version}
Provides:       tex(t1-romandeadf-alt-yrddi.tfm) = %{tl_version}
Provides:       tex(t1-romandeadf-alt-yrdr.tfm) = %{tl_version}
Provides:       tex(t1-romandeadf-alt-yrdri.tfm) = %{tl_version}
Provides:       tex(t1-romandeadf-alt-yrdriw.tfm) = %{tl_version}
Provides:       tex(t1-romandeadf-yrdd.tfm) = %{tl_version}
Provides:       tex(t1-romandeadf-yrddc.tfm) = %{tl_version}
Provides:       tex(t1-romandeadf-yrddi.tfm) = %{tl_version}
Provides:       tex(t1-romandeadf-yrdr.tfm) = %{tl_version}
Provides:       tex(t1-romandeadf-yrdrc.tfm) = %{tl_version}
Provides:       tex(t1-romandeadf-yrdri.tfm) = %{tl_version}
Provides:       tex(t1-romandeadf-yrdriw.tfm) = %{tl_version}
Provides:       tex(ts1-yrdd.tfm) = %{tl_version}, tex(ts1-yrddi.tfm) = %{tl_version}
Provides:       tex(ts1-yrdr.tfm) = %{tl_version}, tex(ts1-yrdri.tfm) = %{tl_version}
Provides:       tex(ts1-yrdriw.tfm) = %{tl_version}, tex(yrdd8c.tfm) = %{tl_version}
Provides:       tex(yrdd8t.tfm) = %{tl_version}, tex(yrdda8t.tfm) = %{tl_version}
Provides:       tex(yrddai8t.tfm) = %{tl_version}, tex(yrddc8t.tfm) = %{tl_version}
Provides:       tex(yrddi8c.tfm) = %{tl_version}, tex(yrddi8t.tfm) = %{tl_version}
Provides:       tex(yrdr8c.tfm) = %{tl_version}, tex(yrdr8t.tfm) = %{tl_version}
Provides:       tex(yrdra8t.tfm) = %{tl_version}, tex(yrdrai8t.tfm) = %{tl_version}
Provides:       tex(yrdraiw8t.tfm) = %{tl_version}, tex(yrdrc8t.tfm) = %{tl_version}
Provides:       tex(yrdri8c.tfm) = %{tl_version}, tex(yrdri8t.tfm) = %{tl_version}
Provides:       tex(yrdriw8c.tfm) = %{tl_version}, tex(yrdriw8t.tfm) = %{tl_version}
Provides:       tex(yrdd8a.pfb) = %{tl_version}, tex(yrddc8a.pfb) = %{tl_version}
Provides:       tex(yrddi8a.pfb) = %{tl_version}, tex(yrdr8a.pfb) = %{tl_version}
Provides:       tex(yrdrc8a.pfb) = %{tl_version}, tex(yrdri8a.pfb) = %{tl_version}
Provides:       tex(yrdriw8a.pfb) = %{tl_version}, tex(yrdd8c.vf) = %{tl_version}
Provides:       tex(yrdd8t.vf) = %{tl_version}, tex(yrdda8t.vf) = %{tl_version}
Provides:       tex(yrddai8t.vf) = %{tl_version}, tex(yrddc8t.vf) = %{tl_version}
Provides:       tex(yrddi8c.vf) = %{tl_version}, tex(yrddi8t.vf) = %{tl_version}
Provides:       tex(yrdr8c.vf) = %{tl_version}, tex(yrdr8t.vf) = %{tl_version}
Provides:       tex(yrdra8t.vf) = %{tl_version}, tex(yrdrai8t.vf) = %{tl_version}
Provides:       tex(yrdraiw8t.vf) = %{tl_version}, tex(yrdrc8t.vf) = %{tl_version}
Provides:       tex(yrdri8c.vf) = %{tl_version}, tex(yrdri8t.vf) = %{tl_version}
Provides:       tex(yrdriw8c.vf) = %{tl_version}, tex(yrdriw8t.vf) = %{tl_version}
Provides:       tex(romande.sty) = %{tl_version}, tex(t1yrd.fd) = %{tl_version}
Provides:       tex(t1yrda.fd) = %{tl_version}, tex(t1yrdaw.fd) = %{tl_version}
Provides:       tex(t1yrdw.fd) = %{tl_version}, tex(ts1yrd.fd) = %{tl_version}
Provides:       tex(ts1yrda.fd) = %{tl_version}, tex(ts1yrdaw.fd) = %{tl_version}
Provides:       tex(ts1yrdw.fd) = %{tl_version}

%description -n texlive-romande
Romande ADF is a serif font family with oldstyle figures,
designed as a substitute for Times, Tiffany or Caslon. The
family currently includes upright, italic and small-caps shapes
in each of regular and demi-bold weights and an italic script
in regular. The support package renames the fonts according to
the Karl Berry fontname scheme and defines four families. Two
of these primarily provide access to the "standard" or default
characters while the "alternate" families support alternate
characters, additional ligatures and the long s. The included
package files provide access to these features in LaTeX as
explained in the documentation. The LaTeX support requires the
nfssext-cfr and the xkeyval packages.

%package -n texlive-romande-doc
Summary:        Documentation for romande
Version:        svn19537.1.008_v7_sc

Provides:       tex-romande-doc
AutoReqProv:    No

%description -n texlive-romande-doc
Documentation for romande

%package -n texlive-rsfso
Provides:       tex-rsfso = %{tl_version}
License:        LPPL
Summary:        A mathematical calligraphic font based on rsfs
Version:        svn37965.1.02

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(xkeyval.sty)
Provides:       tex(rsfso.map) = %{tl_version}, tex(rrsfso10.tfm) = %{tl_version}
Provides:       tex(rrsfso5.tfm) = %{tl_version}, tex(rrsfso7.tfm) = %{tl_version}
Provides:       tex(rsfso10.tfm) = %{tl_version}, tex(rsfso5.tfm) = %{tl_version}
Provides:       tex(rsfso7.tfm) = %{tl_version}, tex(rsfso10.vf) = %{tl_version}
Provides:       tex(rsfso5.vf) = %{tl_version}, tex(rsfso7.vf) = %{tl_version}
Provides:       tex(rsfso.sty) = %{tl_version}, tex(ursfso.fd) = %{tl_version}

%description -n texlive-rsfso
The package provides virtual fonts and LaTeX support files for
mathematical calligraphic fonts based on the rsfs Adobe Type 1
fonts (which must also be present for successful installation,
with the slant substantially reduced. The output is quite
similar to that from the Adobe Mathematical Pi script font.

%package -n texlive-rsfso-doc
Summary:        Documentation for rsfso
Version:        svn37965.1.02

Provides:       tex-rsfso-doc
AutoReqProv:    No

%description -n texlive-rsfso-doc
Documentation for rsfso

%package -n texlive-sansmathaccent
Provides:       tex-sansmathaccent = %{tl_version}
License:        LPPL 1.3
Summary:        Correct placement of accents in sans-serif maths
Version:        svn30187.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(filehook.sty)
Provides:       tex(sansmathaccent.map) = %{tl_version}, tex(mathkerncmssi10.tfm) = %{tl_version}
Provides:       tex(mathkerncmssi12.tfm) = %{tl_version}
Provides:       tex(mathkerncmssi17.tfm) = %{tl_version}
Provides:       tex(mathkerncmssi8.tfm) = %{tl_version}, tex(mathkerncmssi9.tfm) = %{tl_version}
Provides:       tex(mathkerncmssxi10.tfm) = %{tl_version}
Provides:       tex(mathkerncmssxi12.tfm) = %{tl_version}
Provides:       tex(mathkerncmssxi17.tfm) = %{tl_version}
Provides:       tex(mathkerncmssxi8.tfm) = %{tl_version}
Provides:       tex(mathkerncmssxi9.tfm) = %{tl_version}
Provides:       tex(mathkerncmssxi10.vf) = %{tl_version}
Provides:       tex(mathkerncmssxi12.vf) = %{tl_version}
Provides:       tex(mathkerncmssxi17.vf) = %{tl_version}
Provides:       tex(mathkerncmssxi8.vf) = %{tl_version}, tex(mathkerncmssxi9.vf) = %{tl_version}
Provides:       tex(ot1mathkerncmss.fd) = %{tl_version}, tex(sansmathaccent.sty) = %{tl_version}

%description -n texlive-sansmathaccent
Sans serif maths (produced by the beamer class or the sfmath
package) often has accents positioned incorrectly. The package
fixes the positioning of such accents when the default font
(cmssi) is used for sans serif maths.

%package -n texlive-sansmathaccent-doc
Summary:        Documentation for sansmathaccent
Version:        svn30187.0

Provides:       tex-sansmathaccent-doc
AutoReqProv:    No

%description -n texlive-sansmathaccent-doc
Documentation for sansmathaccent

%package -n texlive-sansmathfonts
Provides:       tex-sansmathfonts = %{tl_version}
License:        LPPL 1.3
Summary:        Correct placement of accents in sans-serif maths
Version:        svn43252
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Provides:       tex(sansmathfonts.map) = %{tl_version}, tex(cmsmf10.tfm) = %{tl_version}
Provides:       tex(cmsmf12.tfm) = %{tl_version}, tex(cmsmf17.tfm) = %{tl_version}
Provides:       tex(cmsmf8.tfm) = %{tl_version}, tex(cmsmf9.tfm) = %{tl_version}
Provides:       tex(cmsmfIPiXi10.tfm) = %{tl_version}, tex(cmsmfIPiXi12.tfm) = %{tl_version}
Provides:       tex(cmsmfIPiXi17.tfm) = %{tl_version}, tex(cmsmfIPiXi8.tfm) = %{tl_version}
Provides:       tex(cmsmfIPiXi9.tfm) = %{tl_version}, tex(cmsmfIPiXibx10.tfm) = %{tl_version}
Provides:       tex(cmsmfIPiXibx12.tfm) = %{tl_version}, tex(cmsmfIPiXibx17.tfm) = %{tl_version}
Provides:       tex(cmsmfIPiXibx8.tfm) = %{tl_version}, tex(cmsmfIPiXibx9.tfm) = %{tl_version}
Provides:       tex(cmsmfIPiXibxcsc10.tfm) = %{tl_version}
Provides:       tex(cmsmfIPiXicsc10.tfm) = %{tl_version}
Provides:       tex(cmsmfIPiXicsc8.tfm) = %{tl_version}, tex(cmsmfIPiXicsc9.tfm) = %{tl_version}
Provides:       tex(cmsmfIPiXicsci10.tfm) = %{tl_version}
Provides:       tex(cmsmfIPiXicsci8.tfm) = %{tl_version}
Provides:       tex(cmsmfIPiXicsci9.tfm) = %{tl_version}
Provides:       tex(cmsmfIPiXii10.tfm) = %{tl_version}, tex(cmsmfIPiXii12.tfm) = %{tl_version}
Provides:       tex(cmsmfIPiXii17.tfm) = %{tl_version}, tex(cmsmfIPiXii8.tfm) = %{tl_version}
Provides:       tex(cmsmfIPiXii9.tfm) = %{tl_version}, tex(cmsmfIPiXixi10.tfm) = %{tl_version}
Provides:       tex(cmsmfIPiXixi12.tfm) = %{tl_version}, tex(cmsmfIPiXixi17.tfm) = %{tl_version}
Provides:       tex(cmsmfIPiXixi8.tfm) = %{tl_version}, tex(cmsmfIPiXixi9.tfm) = %{tl_version}
Provides:       tex(cmsmfIPiXixicsc10.tfm) = %{tl_version}
Provides:       tex(cmsmfbx10.tfm) = %{tl_version}, tex(cmsmfbx12.tfm) = %{tl_version}
Provides:       tex(cmsmfbx17.tfm) = %{tl_version}, tex(cmsmfbx8.tfm) = %{tl_version}
Provides:       tex(cmsmfbx9.tfm) = %{tl_version}, tex(cmsmfbxcsc10.tfm) = %{tl_version}
Provides:       tex(cmsmfcsc10.tfm) = %{tl_version}, tex(cmsmfcsc8.tfm) = %{tl_version}
Provides:       tex(cmsmfcsc9.tfm) = %{tl_version}, tex(cmsmfcsci10.tfm) = %{tl_version}
Provides:       tex(cmsmfcsci8.tfm) = %{tl_version}, tex(cmsmfcsci9.tfm) = %{tl_version}
Provides:       tex(cmsmfi10.tfm) = %{tl_version}, tex(cmsmfi12.tfm) = %{tl_version}
Provides:       tex(cmsmfi17.tfm) = %{tl_version}, tex(cmsmfi8.tfm) = %{tl_version}
Provides:       tex(cmsmfi9.tfm) = %{tl_version}, tex(cmsmfxi10.tfm) = %{tl_version}
Provides:       tex(cmsmfxi12.tfm) = %{tl_version}, tex(cmsmfxi17.tfm) = %{tl_version}
Provides:       tex(cmsmfxi8.tfm) = %{tl_version}, tex(cmsmfxi9.tfm) = %{tl_version}
Provides:       tex(cmsmfxicsc10.tfm) = %{tl_version}, tex(cmssbsy10.tfm) = %{tl_version}
Provides:       tex(cmssbsy5.tfm) = %{tl_version}, tex(cmssbsy6.tfm) = %{tl_version}
Provides:       tex(cmssbsy7.tfm) = %{tl_version}, tex(cmssbsy8.tfm) = %{tl_version}
Provides:       tex(cmssbsy9.tfm) = %{tl_version}, tex(cmssbxcsc10.tfm) = %{tl_version}
Provides:       tex(cmsscsc10.tfm) = %{tl_version}, tex(cmsscsc8.tfm) = %{tl_version}
Provides:       tex(cmsscsc9.tfm) = %{tl_version}, tex(cmsscsci10.tfm) = %{tl_version}
Provides:       tex(cmsscsci8.tfm) = %{tl_version}, tex(cmsscsci9.tfm) = %{tl_version}
Provides:       tex(cmssex10.tfm) = %{tl_version}, tex(cmssex7.tfm) = %{tl_version}
Provides:       tex(cmssex8.tfm) = %{tl_version}, tex(cmssex9.tfm) = %{tl_version}
Provides:       tex(cmssmi10.tfm) = %{tl_version}, tex(cmssmi5.tfm) = %{tl_version}
Provides:       tex(cmssmi6.tfm) = %{tl_version}, tex(cmssmi7.tfm) = %{tl_version}
Provides:       tex(cmssmi8.tfm) = %{tl_version}, tex(cmssmi9.tfm) = %{tl_version}
Provides:       tex(cmssmib10.tfm) = %{tl_version}, tex(cmssmib5.tfm) = %{tl_version}
Provides:       tex(cmssmib6.tfm) = %{tl_version}, tex(cmssmib7.tfm) = %{tl_version}
Provides:       tex(cmssmib8.tfm) = %{tl_version}, tex(cmssmib9.tfm) = %{tl_version}
Provides:       tex(cmsssy10.tfm) = %{tl_version}, tex(cmsssy5.tfm) = %{tl_version}
Provides:       tex(cmsssy6.tfm) = %{tl_version}, tex(cmsssy7.tfm) = %{tl_version}
Provides:       tex(cmsssy8.tfm) = %{tl_version}, tex(cmsssy9.tfm) = %{tl_version}
Provides:       tex(cmssu10.tfm) = %{tl_version}, tex(cmssxicsc10.tfm) = %{tl_version}
Provides:       tex(eczi0500.tfm) = %{tl_version}, tex(eczi0600.tfm) = %{tl_version}
Provides:       tex(eczi0700.tfm) = %{tl_version}, tex(eczi0800.tfm) = %{tl_version}
Provides:       tex(eczi0900.tfm) = %{tl_version}, tex(eczi1000.tfm) = %{tl_version}
Provides:       tex(eczi1095.tfm) = %{tl_version}, tex(eczi1200.tfm) = %{tl_version}
Provides:       tex(eczi1440.tfm) = %{tl_version}, tex(eczi1728.tfm) = %{tl_version}
Provides:       tex(eczi2074.tfm) = %{tl_version}, tex(eczi2488.tfm) = %{tl_version}
Provides:       tex(eczi2986.tfm) = %{tl_version}, tex(eczi3583.tfm) = %{tl_version}
Provides:       tex(eczo0500.tfm) = %{tl_version}, tex(eczo0600.tfm) = %{tl_version}
Provides:       tex(eczo0700.tfm) = %{tl_version}, tex(eczo0800.tfm) = %{tl_version}
Provides:       tex(eczo0900.tfm) = %{tl_version}, tex(eczo1000.tfm) = %{tl_version}
Provides:       tex(eczo1095.tfm) = %{tl_version}, tex(eczo1200.tfm) = %{tl_version}
Provides:       tex(eczo1440.tfm) = %{tl_version}, tex(eczo1728.tfm) = %{tl_version}
Provides:       tex(eczo2074.tfm) = %{tl_version}, tex(eczo2488.tfm) = %{tl_version}
Provides:       tex(eczo2986.tfm) = %{tl_version}, tex(eczo3583.tfm) = %{tl_version}
Provides:       tex(eczx0500.tfm) = %{tl_version}, tex(eczx0600.tfm) = %{tl_version}
Provides:       tex(eczx0700.tfm) = %{tl_version}, tex(eczx0800.tfm) = %{tl_version}
Provides:       tex(eczx0900.tfm) = %{tl_version}, tex(eczx1000.tfm) = %{tl_version}
Provides:       tex(eczx1095.tfm) = %{tl_version}, tex(eczx1200.tfm) = %{tl_version}
Provides:       tex(eczx1440.tfm) = %{tl_version}, tex(eczx1728.tfm) = %{tl_version}
Provides:       tex(eczx2074.tfm) = %{tl_version}, tex(eczx2488.tfm) = %{tl_version}
Provides:       tex(eczx2986.tfm) = %{tl_version}, tex(eczx3583.tfm) = %{tl_version}
Provides:       tex(eczz0500.tfm) = %{tl_version}, tex(eczz0600.tfm) = %{tl_version}
Provides:       tex(eczz0700.tfm) = %{tl_version}, tex(eczz0800.tfm) = %{tl_version}
Provides:       tex(eczz0900.tfm) = %{tl_version}, tex(eczz1000.tfm) = %{tl_version}
Provides:       tex(eczz1095.tfm) = %{tl_version}, tex(eczz1200.tfm) = %{tl_version}
Provides:       tex(eczz1440.tfm) = %{tl_version}, tex(eczz1728.tfm) = %{tl_version}
Provides:       tex(eczz2074.tfm) = %{tl_version}, tex(eczz2488.tfm) = %{tl_version}
Provides:       tex(eczz2986.tfm) = %{tl_version}, tex(eczz3583.tfm) = %{tl_version}
Provides:       tex(ssesint10.tfm) = %{tl_version}, tex(ssesint7.tfm) = %{tl_version}
Provides:       tex(ssesint8.tfm) = %{tl_version}, tex(ssesint9.tfm) = %{tl_version}
Provides:       tex(ssmsam10.tfm) = %{tl_version}, tex(ssmsam5.tfm) = %{tl_version}
Provides:       tex(ssmsam6.tfm) = %{tl_version}, tex(ssmsam7.tfm) = %{tl_version}
Provides:       tex(ssmsam8.tfm) = %{tl_version}, tex(ssmsam9.tfm) = %{tl_version}
Provides:       tex(ssmsbm10.tfm) = %{tl_version}, tex(ssmsbm5.tfm) = %{tl_version}
Provides:       tex(ssmsbm6.tfm) = %{tl_version}, tex(ssmsbm7.tfm) = %{tl_version}
Provides:       tex(ssmsbm8.tfm) = %{tl_version}, tex(ssmsbm9.tfm) = %{tl_version}
Provides:       tex(cmsmfIPiXi10.pfb) = %{tl_version}, tex(cmsmfIPiXi12.pfb) = %{tl_version}
Provides:       tex(cmsmfIPiXi17.pfb) = %{tl_version}, tex(cmsmfIPiXi8.pfb) = %{tl_version}
Provides:       tex(cmsmfIPiXi9.pfb) = %{tl_version}, tex(cmsmfIPiXibx10.pfb) = %{tl_version}
Provides:       tex(cmsmfIPiXibx12.pfb) = %{tl_version}, tex(cmsmfIPiXibx17.pfb) = %{tl_version}
Provides:       tex(cmsmfIPiXibx8.pfb) = %{tl_version}, tex(cmsmfIPiXibx9.pfb) = %{tl_version}
Provides:       tex(cmsmfIPiXibxcsc10.pfb) = %{tl_version}
Provides:       tex(cmsmfIPiXicsc10.pfb) = %{tl_version}
Provides:       tex(cmsmfIPiXicsc8.pfb) = %{tl_version}, tex(cmsmfIPiXicsc9.pfb) = %{tl_version}
Provides:       tex(cmsmfIPiXicsci10.pfb) = %{tl_version}
Provides:       tex(cmsmfIPiXicsci8.pfb) = %{tl_version}
Provides:       tex(cmsmfIPiXicsci9.pfb) = %{tl_version}
Provides:       tex(cmsmfIPiXii10.pfb) = %{tl_version}, tex(cmsmfIPiXii12.pfb) = %{tl_version}
Provides:       tex(cmsmfIPiXii17.pfb) = %{tl_version}, tex(cmsmfIPiXii8.pfb) = %{tl_version}
Provides:       tex(cmsmfIPiXii9.pfb) = %{tl_version}, tex(cmsmfIPiXixi10.pfb) = %{tl_version}
Provides:       tex(cmsmfIPiXixi12.pfb) = %{tl_version}, tex(cmsmfIPiXixi17.pfb) = %{tl_version}
Provides:       tex(cmsmfIPiXixi8.pfb) = %{tl_version}, tex(cmsmfIPiXixi9.pfb) = %{tl_version}
Provides:       tex(cmsmfIPiXixicsc10.pfb) = %{tl_version}
Provides:       tex(cmssbsy10.pfb) = %{tl_version}, tex(cmssbsy5.pfb) = %{tl_version}
Provides:       tex(cmssbsy6.pfb) = %{tl_version}, tex(cmssbsy7.pfb) = %{tl_version}
Provides:       tex(cmssbsy8.pfb) = %{tl_version}, tex(cmssbsy9.pfb) = %{tl_version}
Provides:       tex(cmssbx12.pfb) = %{tl_version}, tex(cmssbx17.pfb) = %{tl_version}
Provides:       tex(cmssbx8.pfb) = %{tl_version}, tex(cmssbx9.pfb) = %{tl_version}
Provides:       tex(cmssbxcsc10.pfb) = %{tl_version}, tex(cmsscsc10.pfb) = %{tl_version}
Provides:       tex(cmsscsc8.pfb) = %{tl_version}, tex(cmsscsc9.pfb) = %{tl_version}
Provides:       tex(cmsscsci10.pfb) = %{tl_version}, tex(cmsscsci8.pfb) = %{tl_version}
Provides:       tex(cmsscsci9.pfb) = %{tl_version}, tex(cmssex10.pfb) = %{tl_version}
Provides:       tex(cmssex7.pfb) = %{tl_version}, tex(cmssex8.pfb) = %{tl_version}
Provides:       tex(cmssex9.pfb) = %{tl_version}, tex(cmssmi10.pfb) = %{tl_version}
Provides:       tex(cmssmi5.pfb) = %{tl_version}, tex(cmssmi6.pfb) = %{tl_version}
Provides:       tex(cmssmi7.pfb) = %{tl_version}, tex(cmssmi8.pfb) = %{tl_version}
Provides:       tex(cmssmi9.pfb) = %{tl_version}, tex(cmssmib10.pfb) = %{tl_version}
Provides:       tex(cmssmib5.pfb) = %{tl_version}, tex(cmssmib6.pfb) = %{tl_version}
Provides:       tex(cmssmib7.pfb) = %{tl_version}, tex(cmssmib8.pfb) = %{tl_version}
Provides:       tex(cmssmib9.pfb) = %{tl_version}, tex(cmsssy10.pfb) = %{tl_version}
Provides:       tex(cmsssy5.pfb) = %{tl_version}, tex(cmsssy6.pfb) = %{tl_version}
Provides:       tex(cmsssy7.pfb) = %{tl_version}, tex(cmsssy8.pfb) = %{tl_version}
Provides:       tex(cmsssy9.pfb) = %{tl_version}, tex(cmssu10.pfb) = %{tl_version}
Provides:       tex(cmssxi10.pfb) = %{tl_version}, tex(cmssxi12.pfb) = %{tl_version}
Provides:       tex(cmssxi17.pfb) = %{tl_version}, tex(cmssxi8.pfb) = %{tl_version}
Provides:       tex(cmssxi9.pfb) = %{tl_version}, tex(cmssxicsc10.pfb) = %{tl_version}
Provides:       tex(eczi0500.pfb) = %{tl_version}, tex(eczi0600.pfb) = %{tl_version}
Provides:       tex(eczi0700.pfb) = %{tl_version}, tex(eczi0800.pfb) = %{tl_version}
Provides:       tex(eczi0900.pfb) = %{tl_version}, tex(eczi1000.pfb) = %{tl_version}
Provides:       tex(eczi1095.pfb) = %{tl_version}, tex(eczi1200.pfb) = %{tl_version}
Provides:       tex(eczi1440.pfb) = %{tl_version}, tex(eczi1728.pfb) = %{tl_version}
Provides:       tex(eczi2074.pfb) = %{tl_version}, tex(eczi2488.pfb) = %{tl_version}
Provides:       tex(eczi2986.pfb) = %{tl_version}, tex(eczi3583.pfb) = %{tl_version}
Provides:       tex(eczo0500.pfb) = %{tl_version}, tex(eczo0600.pfb) = %{tl_version}
Provides:       tex(eczo0700.pfb) = %{tl_version}, tex(eczo0800.pfb) = %{tl_version}
Provides:       tex(eczo0900.pfb) = %{tl_version}, tex(eczo1000.pfb) = %{tl_version}
Provides:       tex(eczo1095.pfb) = %{tl_version}, tex(eczo1200.pfb) = %{tl_version}
Provides:       tex(eczo1440.pfb) = %{tl_version}, tex(eczo1728.pfb) = %{tl_version}
Provides:       tex(eczo2074.pfb) = %{tl_version}, tex(eczo2488.pfb) = %{tl_version}
Provides:       tex(eczo2986.pfb) = %{tl_version}, tex(eczo3583.pfb) = %{tl_version}
Provides:       tex(eczx0500.pfb) = %{tl_version}, tex(eczx0600.pfb) = %{tl_version}
Provides:       tex(eczx0700.pfb) = %{tl_version}, tex(eczx0800.pfb) = %{tl_version}
Provides:       tex(eczx0900.pfb) = %{tl_version}, tex(eczx1000.pfb) = %{tl_version}
Provides:       tex(eczx1095.pfb) = %{tl_version}, tex(eczx1200.pfb) = %{tl_version}
Provides:       tex(eczx1440.pfb) = %{tl_version}, tex(eczx1728.pfb) = %{tl_version}
Provides:       tex(eczx2074.pfb) = %{tl_version}, tex(eczx2488.pfb) = %{tl_version}
Provides:       tex(eczx2986.pfb) = %{tl_version}, tex(eczx3583.pfb) = %{tl_version}
Provides:       tex(eczz0500.pfb) = %{tl_version}, tex(eczz0600.pfb) = %{tl_version}
Provides:       tex(eczz0700.pfb) = %{tl_version}, tex(eczz0800.pfb) = %{tl_version}
Provides:       tex(eczz0900.pfb) = %{tl_version}, tex(eczz1000.pfb) = %{tl_version}
Provides:       tex(eczz1095.pfb) = %{tl_version}, tex(eczz1200.pfb) = %{tl_version}
Provides:       tex(eczz1440.pfb) = %{tl_version}, tex(eczz1728.pfb) = %{tl_version}
Provides:       tex(eczz2074.pfb) = %{tl_version}, tex(eczz2488.pfb) = %{tl_version}
Provides:       tex(eczz2986.pfb) = %{tl_version}, tex(eczz3583.pfb) = %{tl_version}
Provides:       tex(ssesint10.pfb) = %{tl_version}, tex(ssesint7.pfb) = %{tl_version}
Provides:       tex(ssesint8.pfb) = %{tl_version}, tex(ssesint9.pfb) = %{tl_version}
Provides:       tex(ssmsam10.pfb) = %{tl_version}, tex(ssmsam5.pfb) = %{tl_version}
Provides:       tex(ssmsam6.pfb) = %{tl_version}, tex(ssmsam7.pfb) = %{tl_version}
Provides:       tex(ssmsam8.pfb) = %{tl_version}, tex(ssmsam9.pfb) = %{tl_version}
Provides:       tex(ssmsbm10.pfb) = %{tl_version}, tex(ssmsbm5.pfb) = %{tl_version}
Provides:       tex(ssmsbm6.pfb) = %{tl_version}, tex(ssmsbm7.pfb) = %{tl_version}
Provides:       tex(ssmsbm8.pfb) = %{tl_version}, tex(ssmsbm9.pfb) = %{tl_version}
Provides:       tex(cmsmf10.vf) = %{tl_version}, tex(cmsmf12.vf) = %{tl_version}
Provides:       tex(cmsmf17.vf) = %{tl_version}, tex(cmsmf8.vf) = %{tl_version}
Provides:       tex(cmsmf9.vf) = %{tl_version}, tex(cmsmfbx10.vf) = %{tl_version}
Provides:       tex(cmsmfbx12.vf) = %{tl_version}, tex(cmsmfbx17.vf) = %{tl_version}
Provides:       tex(cmsmfbx8.vf) = %{tl_version}, tex(cmsmfbx9.vf) = %{tl_version}
Provides:       tex(cmsmfbxcsc10.vf) = %{tl_version}, tex(cmsmfcsc10.vf) = %{tl_version}
Provides:       tex(cmsmfcsc8.vf) = %{tl_version}, tex(cmsmfcsc9.vf) = %{tl_version}
Provides:       tex(cmsmfcsci10.vf) = %{tl_version}, tex(cmsmfcsci8.vf) = %{tl_version}
Provides:       tex(cmsmfcsci9.vf) = %{tl_version}, tex(cmsmfi10.vf) = %{tl_version}
Provides:       tex(cmsmfi12.vf) = %{tl_version}, tex(cmsmfi17.vf) = %{tl_version}
Provides:       tex(cmsmfi8.vf) = %{tl_version}, tex(cmsmfi9.vf) = %{tl_version}
Provides:       tex(cmsmfxi10.vf) = %{tl_version}, tex(cmsmfxi12.vf) = %{tl_version}
Provides:       tex(cmsmfxi17.vf) = %{tl_version}, tex(cmsmfxi8.vf) = %{tl_version}
Provides:       tex(cmsmfxi9.vf) = %{tl_version}, tex(cmsmfxicsc10.vf) = %{tl_version}
Provides:       tex(omlcmssm.fd) = %{tl_version}, tex(omscmsssy.fd) = %{tl_version}
Provides:       tex(omxcmssex.fd) = %{tl_version}, tex(ot1cmsmf.fd) = %{tl_version}
Provides:       tex(ot1xcmss.fd) = %{tl_version}, tex(sansmathfonts.sty) = %{tl_version}
Provides:       tex(t1xcmss.fd) = %{tl_version}, tex(ucmsmf.fd) = %{tl_version}
Provides:       tex(ussesint.fd) = %{tl_version}, tex(ussmsa.fd) = %{tl_version}
Provides:       tex(ussmsb.fd) = %{tl_version}, tex(uxcmss.fd) = %{tl_version}

%description -n texlive-sansmathfonts
Sans serifsmall caps and math fonts for use with Computer
Modern.

%package -n texlive-sansmathfonts-doc
Summary:        Documentation for sansmathfonts
Version:        svn43252
Provides:       tex-sansmathfonts-doc
AutoReqProv:    No

%description -n texlive-sansmathfonts-doc
Documentation for sansmathfonts

%package -n texlive-sanskrit
Provides:       tex-sanskrit = %{tl_version}
License:        LPPL
Summary:        Sanskrit support
Version:        svn42925
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(relsize.sty), tex(ifthen.sty)
Provides:       tex(skt10.tfm) = %{tl_version}, tex(skt8.tfm) = %{tl_version}
Provides:       tex(skt9.tfm) = %{tl_version}, tex(sktb10.tfm) = %{tl_version}
Provides:       tex(sktbs10.tfm) = %{tl_version}, tex(sktf10.tfm) = %{tl_version}
Provides:       tex(sktfs10.tfm) = %{tl_version}, tex(skts10.tfm) = %{tl_version}
Provides:       tex(ot1skt.fd) = %{tl_version}, tex(skt.sty) = %{tl_version}

%description -n texlive-sanskrit
A font and pre-processor suitable for the production of
documents written in Sanskrit. Type 1 versions of the fonts are
available.

%package -n texlive-sanskrit-doc
Summary:        Documentation for sanskrit
Version:        svn42925
Provides:       tex-sanskrit-doc
AutoReqProv:    No

%description -n texlive-sanskrit-doc
Documentation for sanskrit

%package -n texlive-sanskrit-t1
Provides:       tex-sanskrit-t1 = %{tl_version}
License:        LPPL
Summary:        Type 1 version of 'skt' fonts for Sanskrit
Version:        svn35737.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(skt.map) = %{tl_version}, tex(skt10.pfb) = %{tl_version}
Provides:       tex(skt8.pfb) = %{tl_version}, tex(skt9.pfb) = %{tl_version}
Provides:       tex(sktb10.pfb) = %{tl_version}, tex(sktbs10.pfb) = %{tl_version}
Provides:       tex(sktf10.pfb) = %{tl_version}, tex(sktfs10.pfb) = %{tl_version}
Provides:       tex(skts10.pfb) = %{tl_version}

%description -n texlive-sanskrit-t1
The sanskrit-t1 font package provides Type 1 version of Charles
Wikner's skt font series for the Sanskrit language.

%package -n texlive-sanskrit-t1-doc
Summary:        Documentation for sanskrit-t1
Version:        svn35737.0

Provides:       tex-sanskrit-t1-doc
AutoReqProv:    No

%description -n texlive-sanskrit-t1-doc
Documentation for sanskrit-t1

%package -n texlive-sauter
Provides:       tex-sauter = %{tl_version}
License:        GPL+
Summary:        Wide range of design sizes for CM fonts
Version:        svn13293.2.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-sauter
Extensions, originally to the CM fonts, providing a
parameterization scheme to build Metafont fonts at true design
sizes, for a large range of sizes. The scheme has now been
extended to a range of other fonts, including the AMS fonts,
bbm, bbold, rsfs and wasy fonts.

%package -n texlive-sauterfonts
Provides:       tex-sauterfonts = %{tl_version}
License:        GPL+
Summary:        Use Sauter's fonts in LaTeX
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(sbbm.sty) = %{tl_version}, tex(sexscale.sty) = %{tl_version}
Provides:       tex(somlcmm.fd) = %{tl_version}, tex(somlcmr.fd) = %{tl_version}
Provides:       tex(somscmr.fd) = %{tl_version}, tex(somscmsy.fd) = %{tl_version}
Provides:       tex(somxcmex.fd) = %{tl_version}, tex(sot1cmdh.fd) = %{tl_version}
Provides:       tex(sot1cmfib.fd) = %{tl_version}, tex(sot1cmfr.fd) = %{tl_version}
Provides:       tex(sot1cmr.fd) = %{tl_version}, tex(sot1cmss.fd) = %{tl_version}
Provides:       tex(sot1cmtt.fd) = %{tl_version}, tex(sot1cmvtt.fd) = %{tl_version}
Provides:       tex(subbm.fd) = %{tl_version}, tex(subbmdh.fd) = %{tl_version}
Provides:       tex(subbmfib.fd) = %{tl_version}, tex(subbmss.fd) = %{tl_version}
Provides:       tex(subbmtt.fd) = %{tl_version}, tex(subbmvtt.fd) = %{tl_version}
Provides:       tex(subbold.fd) = %{tl_version}, tex(sucmr.fd) = %{tl_version}
Provides:       tex(sucmss.fd) = %{tl_version}, tex(sucmtt.fd) = %{tl_version}
Provides:       tex(sulasy.fd) = %{tl_version}, tex(sumsa.fd) = %{tl_version}
Provides:       tex(sumsb.fd) = %{tl_version}, tex(sursfs.fd) = %{tl_version}
Provides:       tex(sustmry.fd) = %{tl_version}, tex(suwasy.fd) = %{tl_version}

%description -n texlive-sauterfonts
The package provides font definition files (plus a replacement
for the package exscale) to access many of the fonts in
Sauter's collection. These fonts are available in all point
sizes and look nicer for such "intermediate" document sizes as
11pt. Also included is the package sbbm, an alternative to
access the bbm fonts.

%package -n texlive-sauterfonts-doc
Summary:        Documentation for sauterfonts
Version:        svn15878.0

Provides:       tex-sauterfonts-doc
AutoReqProv:    No

%description -n texlive-sauterfonts-doc
Documentation for sauterfonts

%package -n texlive-schulschriften
Provides:       tex-schulschriften = %{tl_version}
License:        LPPL
Summary:        German "school scripts" from Suetterlin to the present day
Version:        svn35730.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(wedn14.tfm) = %{tl_version}, tex(wednbx14.tfm) = %{tl_version}
Provides:       tex(wednbxsl14.tfm) = %{tl_version}, tex(wedneb14.tfm) = %{tl_version}
Provides:       tex(wednebsl14.tfm) = %{tl_version}, tex(wednsb14.tfm) = %{tl_version}
Provides:       tex(wednsbsl14.tfm) = %{tl_version}, tex(wednsl14.tfm) = %{tl_version}
Provides:       tex(wednub14.tfm) = %{tl_version}, tex(wednubsl14.tfm) = %{tl_version}
Provides:       tex(wela14.tfm) = %{tl_version}, tex(welabx14.tfm) = %{tl_version}
Provides:       tex(welabxsl14.tfm) = %{tl_version}, tex(welaeb14.tfm) = %{tl_version}
Provides:       tex(welaebsl14.tfm) = %{tl_version}, tex(welasb14.tfm) = %{tl_version}
Provides:       tex(welasbsl14.tfm) = %{tl_version}, tex(welasl14.tfm) = %{tl_version}
Provides:       tex(welaub14.tfm) = %{tl_version}, tex(welaubsl14.tfm) = %{tl_version}
Provides:       tex(wesa14.tfm) = %{tl_version}, tex(wesabx14.tfm) = %{tl_version}
Provides:       tex(wesabxsl14.tfm) = %{tl_version}, tex(wesaeb14.tfm) = %{tl_version}
Provides:       tex(wesaebsl14.tfm) = %{tl_version}, tex(wesasb14.tfm) = %{tl_version}
Provides:       tex(wesasbsl14.tfm) = %{tl_version}, tex(wesasl14.tfm) = %{tl_version}
Provides:       tex(wesaub14.tfm) = %{tl_version}, tex(wesaubsl14.tfm) = %{tl_version}
Provides:       tex(wesu14.tfm) = %{tl_version}, tex(wesub14.tfm) = %{tl_version}
Provides:       tex(wesubsl14.tfm) = %{tl_version}, tex(wesubx14.tfm) = %{tl_version}
Provides:       tex(wesubxsl14.tfm) = %{tl_version}, tex(wesueb14.tfm) = %{tl_version}
Provides:       tex(wesuebsl14.tfm) = %{tl_version}, tex(wesusb14.tfm) = %{tl_version}
Provides:       tex(wesusbsl14.tfm) = %{tl_version}, tex(wesusl14.tfm) = %{tl_version}
Provides:       tex(wesuub14.tfm) = %{tl_version}, tex(wesuubsl14.tfm) = %{tl_version}
Provides:       tex(weva14.tfm) = %{tl_version}, tex(wevabx14.tfm) = %{tl_version}
Provides:       tex(wevabxsl14.tfm) = %{tl_version}, tex(wevaeb14.tfm) = %{tl_version}
Provides:       tex(wevaebsl14.tfm) = %{tl_version}, tex(wevasb14.tfm) = %{tl_version}
Provides:       tex(wevasbsl14.tfm) = %{tl_version}, tex(wevasl14.tfm) = %{tl_version}
Provides:       tex(wevaub14.tfm) = %{tl_version}, tex(wevaubsl14.tfm) = %{tl_version}
Provides:       tex(schulschriften_lin.sty) = %{tl_version}
Provides:       tex(schulschriften_ltx.sty) = %{tl_version}
Provides:       tex(t1wedn.fd) = %{tl_version}, tex(t1wela.fd) = %{tl_version}
Provides:       tex(t1wesa.fd) = %{tl_version}, tex(t1wesu.fd) = %{tl_version}
Provides:       tex(t1weva.fd) = %{tl_version}, tex(wedn.sty) = %{tl_version}
Provides:       tex(wela.sty) = %{tl_version}, tex(wesa.sty) = %{tl_version}
Provides:       tex(wesu.sty) = %{tl_version}, tex(weva.sty) = %{tl_version}

%description -n texlive-schulschriften
Das Paket enthalt im wesentlichen die METAFONT-Quellfiles fur
die folgenden Schulausgangsschriften: Suetterlinschrift,
Deutsche Normalschrift, Lateinische Ausgangsschrift,
Schulausgangsschrift, Vereinfachte Ausgangsschrift. Damit ist
es moglich, beliebige deutsche Texte in diesen Schreibschriften
zu schreiben.

%package -n texlive-schulschriften-doc
Summary:        Documentation for schulschriften
Version:        svn35730.4

Provides:       tex-schulschriften-doc
AutoReqProv:    No

%description -n texlive-schulschriften-doc
Documentation for schulschriften

%package -n texlive-semaphor
Provides:       tex-semaphor = %{tl_version}
License:        GPL+
Summary:        Semaphore alphabet font
Version:        svn18651.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(smfb10.enc) = %{tl_version}, tex(smfbsl10.enc) = %{tl_version}
Provides:       tex(smfeb10.enc) = %{tl_version}, tex(smfebsl10.enc) = %{tl_version}
Provides:       tex(smfer10.enc) = %{tl_version}, tex(smfesl10.enc) = %{tl_version}
Provides:       tex(smfett10.enc) = %{tl_version}, tex(smfpb10.enc) = %{tl_version}
Provides:       tex(smfpbsl10.enc) = %{tl_version}, tex(smfpr10.enc) = %{tl_version}
Provides:       tex(smfpsl10.enc) = %{tl_version}, tex(smfptt10.enc) = %{tl_version}
Provides:       tex(smfr10.enc) = %{tl_version}, tex(smfsl10.enc) = %{tl_version}
Provides:       tex(smftt10.enc) = %{tl_version}, tex(semaf.map) = %{tl_version}
Provides:       tex(smfb10.otf) = %{tl_version}, tex(smfbsl10.otf) = %{tl_version}
Provides:       tex(smfeb10.otf) = %{tl_version}, tex(smfebsl10.otf) = %{tl_version}
Provides:       tex(smfer10.otf) = %{tl_version}, tex(smfesl10.otf) = %{tl_version}
Provides:       tex(smfett10.otf) = %{tl_version}, tex(smfpb10.otf) = %{tl_version}
Provides:       tex(smfpbsl10.otf) = %{tl_version}, tex(smfpr10.otf) = %{tl_version}
Provides:       tex(smfpsl10.otf) = %{tl_version}, tex(smfptt10.otf) = %{tl_version}
Provides:       tex(smfr10.otf) = %{tl_version}, tex(smfsl10.otf) = %{tl_version}
Provides:       tex(smftt10.otf) = %{tl_version}, tex(smfb10.tfm) = %{tl_version}
Provides:       tex(smfbsl10.tfm) = %{tl_version}, tex(smfeb10.tfm) = %{tl_version}
Provides:       tex(smfebsl10.tfm) = %{tl_version}, tex(smfer10.tfm) = %{tl_version}
Provides:       tex(smfesl10.tfm) = %{tl_version}, tex(smfett10.tfm) = %{tl_version}
Provides:       tex(smfpb10.tfm) = %{tl_version}, tex(smfpbsl10.tfm) = %{tl_version}
Provides:       tex(smfpr10.tfm) = %{tl_version}, tex(smfpsl10.tfm) = %{tl_version}
Provides:       tex(smfptt10.tfm) = %{tl_version}, tex(smfr10.tfm) = %{tl_version}
Provides:       tex(smfsl10.tfm) = %{tl_version}, tex(smftt10.tfm) = %{tl_version}
Provides:       tex(smfb10.pfb) = %{tl_version}, tex(smfbsl10.pfb) = %{tl_version}
Provides:       tex(smfeb10.pfb) = %{tl_version}, tex(smfebsl10.pfb) = %{tl_version}
Provides:       tex(smfer10.pfb) = %{tl_version}, tex(smfesl10.pfb) = %{tl_version}
Provides:       tex(smfett10.pfb) = %{tl_version}, tex(smfpb10.pfb) = %{tl_version}
Provides:       tex(smfpbsl10.pfb) = %{tl_version}, tex(smfpr10.pfb) = %{tl_version}
Provides:       tex(smfpsl10.pfb) = %{tl_version}, tex(smfptt10.pfb) = %{tl_version}
Provides:       tex(smfr10.pfb) = %{tl_version}, tex(smfsl10.pfb) = %{tl_version}
Provides:       tex(smftt10.pfb) = %{tl_version}, tex(t-type-semaf.tex) = %{tl_version}
Provides:       tex(il2semaf.fd) = %{tl_version}, tex(semaf.fd) = %{tl_version}
Provides:       tex(semaf.tex) = %{tl_version}

%description -n texlive-semaphor
These fonts represent semaphore in a highly schematic, but very
clear, fashion. The fonts are provided as Metafont source, and
in both OpenType and Adobe Type 1 formats.

%package -n texlive-semaphor-doc
Summary:        Documentation for semaphor
Version:        svn18651.0

Provides:       tex-semaphor-doc
AutoReqProv:    No

%description -n texlive-semaphor-doc
Documentation for semaphor

%package -n texlive-rsfs
Provides:       tex-rsfs = %{tl_version}
License:        rsfs
Summary:        Ralph Smith's Formal Script font
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(rsfs.map) = %{tl_version}, tex(rsfs10.tfm) = %{tl_version}
Provides:       tex(rsfs5.tfm) = %{tl_version}, tex(rsfs7.tfm) = %{tl_version}
Provides:       tex(rsfs10.pfb) = %{tl_version}, tex(rsfs5.pfb) = %{tl_version}
Provides:       tex(rsfs7.pfb) = %{tl_version}, tex(scrload.tex) = %{tl_version}

%description -n texlive-rsfs
The fonts provide uppercase 'formal' script letters for use as
symbols in scientific and mathematical typesetting (in contrast
to the informal script fonts such as that used for the
'calligraphic' symbols in the TeX maths symbol font). The fonts
are provided as Metafont source, and as derived Adobe Type 1
format. LaTeX support, for using these fonts in mathematics, is
available via one of the packages calrsfs and mathrsfs.

%package -n texlive-rsfs-doc
Summary:        Documentation for rsfs
Version:        svn15878.0

Provides:       tex-rsfs-doc
AutoReqProv:    No

%description -n texlive-rsfs-doc
Documentation for rsfs

%package -n texlive-schwalbe-chess
Provides:       tex-schwalbe-chess = %{tl_version}
License:        LPPL 1.2
Summary:        Typeset the German chess magazine "Die Schwalbe"
Version:        svn48356
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(fontenc.sty), tex(inputenc.sty), tex(babel.sty), tex(ifthen.sty)
Requires:       tex(times.sty), tex(picinpar.sty), tex(multicol.sty), tex(url.sty)
Requires:       tex(diagram.sty)
Provides:       tex(schwalbe.cls) = %{tl_version}, tex(schwalbe.sty) = %{tl_version}

%description -n texlive-schwalbe-chess
The package is based on chess-problem-diagrams, which in its
turn has a dependency on the bartel-chess-fonts

%package -n texlive-schwalbe-chess-doc
Summary:        Documentation for schwalbe-chess
Version:        svn48356
Provides:       tex-schwalbe-chess-doc
AutoReqProv:    No

%description -n texlive-schwalbe-chess-doc
Documentation for schwalbe-chess

%package -n texlive-sgame
Provides:       tex-sgame = %{tl_version}
License:        LPPL
Summary:        LaTeX style for typesetting strategic games
Version:        svn30959.2.15

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(color.sty)
Provides:       tex(sgame.sty) = %{tl_version}, tex(sgamevar.sty) = %{tl_version}

%description -n texlive-sgame
Formats strategic games. For a 2x2 game, for example, the
input: \begin{game}{2}{2} &$L$ &$M$\\ $T$ &$2,2$ &$2,0$\\ $B$
&$3,0$ &$0,9$ \end{game} produces output with (a) boxes around
the payoffs, (b) payoff columns of equal width, and (c) payoffs
vertically centered within the boxes. Note that the game
environment will not work in the argument of another command.

%package -n texlive-sgame-doc
Summary:        Documentation for sgame
Version:        svn30959.2.15

Provides:       tex-sgame-doc
AutoReqProv:    No

%description -n texlive-sgame-doc
Documentation for sgame

%package -n texlive-schemata
Provides:       tex-schemata = %{tl_version}
License:        LPPL 1.3
Summary:        Print topical diagrams
Version:        svn39510

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(schemata.sty) = %{tl_version}

%description -n texlive-schemata
The package facilitates the creation of topical schemata,
outlines that use braces (or facsimiles thereof) to illustrate
the breakdown of concepts and categories in Scholastic thought
from late medieval and early modern periods.

%package -n texlive-schemata-doc
Summary:        Documentation for schemata
Version:        svn39510

Provides:       tex-schemata-doc
AutoReqProv:    No

%description -n texlive-schemata-doc
Documentation for schemata

%package -n texlive-sansmath
Provides:       tex-sansmath = %{tl_version}
License:        Public Domain
Summary:        Maths in a sans font
Version:        svn17997.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(sansmath.sty) = %{tl_version}

%description -n texlive-sansmath
The package defines a new math version sans, and a command
\sansmath that behaves somewhat like \boldmath

%package -n texlive-sansmath-doc
Summary:        Documentation for sansmath
Version:        svn17997.1.1

Provides:       tex-sansmath-doc
AutoReqProv:    No

%description -n texlive-sansmath-doc
Documentation for sansmath

%package -n texlive-section
Provides:       tex-section = %{tl_version}
License:        LPPL
Summary:        Modifying section commands in LaTeX
Version:        svn20180.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(section.sty) = %{tl_version}

%description -n texlive-section
The package implements a pretty extensive scheme to make more
manageable the business of configuring LaTeX output.

%package -n texlive-section-doc
Summary:        Documentation for section
Version:        svn20180.0

Provides:       tex-section-doc
AutoReqProv:    No

%description -n texlive-section-doc
Documentation for section

%package -n texlive-seminar
Provides:       tex-seminar = %{tl_version}
License:        LPPL 1.2
Summary:        Make overhead slides
Version:        svn34011.1.62

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(hyperref.sty), tex(pst-ovl.sty), tex(doc.sty), tex(article.sty)
Requires:       tex(fancybox.sty)
Provides:       tex(npsfont.sty) = %{tl_version}, tex(sem-a4.sty) = %{tl_version}
Provides:       tex(sem-dem.sty) = %{tl_version}, tex(sem-page.sty) = %{tl_version}
Provides:       tex(semcolor.sty) = %{tl_version}, tex(semhelv.sty) = %{tl_version}
Provides:       tex(seminar.bg2) = %{tl_version}, tex(seminar.bug) = %{tl_version}
Provides:       tex(seminar.cls) = %{tl_version}, tex(seminar.sty) = %{tl_version}
Provides:       tex(semlayer.sty) = %{tl_version}, tex(semlcmss.sty) = %{tl_version}
Provides:       tex(semrot.sty) = %{tl_version}, tex(slidesec.sty) = %{tl_version}
Provides:       tex(tvz-code.sty) = %{tl_version}, tex(tvz-hax.sty) = %{tl_version}
Provides:       tex(tvz-user.sty) = %{tl_version}

%description -n texlive-seminar
A class that produces overhead slides (transparencies), with
many facilities. The class requires availability of the
fancybox package. Seminar is also the basis of other classes,
such as prosper. In fact, seminar is not nowadays reckoned a
good basis for a presentation -- users are advised to use more
recent classes such as powerdot or beamer, both of which are
tuned to 21st-century presentation styles. Note that the
seminar distribution relies on the xcomment package, which was
once part of the bundle, but now has a separate existence.

%package -n texlive-seminar-doc
Summary:        Documentation for seminar
Version:        svn34011.1.62

Provides:       tex-seminar-doc
AutoReqProv:    No

%description -n texlive-seminar-doc
Documentation for seminar

%package -n texlive-sepnum
Provides:       tex-sepnum = %{tl_version}
License:        LPPL
Summary:        Print numbers in a "friendly" format
Version:        svn20186.2.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(sepnum.sty) = %{tl_version}

%description -n texlive-sepnum
Provides a command to print a number with (potentially
different) separators every three digits in the parts either
side of the decimal point (the point itself is also
configurable). The macro is fully expandable and not fragile
(unless one of the separators is). There is also a command
\sepnumform, that may be used when defining \the<counter>
macros.

%package -n texlive-sepnum-doc
Summary:        Documentation for sepnum
Version:        svn20186.2.0

Provides:       tex-sepnum-doc
AutoReqProv:    No

%description -n texlive-sepnum-doc
Documentation for sepnum

%package -n texlive-setspace
Provides:       tex-setspace = %{tl_version}
License:        Copyright only
Summary:        Set space between lines
Version:        svn24881.6.7a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(setspace.sty) = %{tl_version}

%description -n texlive-setspace
Provides support for setting the spacing between lines in a
document. Package options include singlespacing,
onehalfspacing, and doublespacing. Alternatively the spacing
can be changed as required with the \singlespacing,
\onehalfspacing, and \doublespacing commands. Other size
spacings also available.

%package -n texlive-setspace-doc
Summary:        Documentation for setspace
Version:        svn24881.6.7a

Provides:       tex-setspace-doc
AutoReqProv:    No

%description -n texlive-setspace-doc
Documentation for setspace

%package -n texlive-rviewport
Provides:       tex-rviewport = %{tl_version}
License:        LPPL
Summary:        Relative Viewport for Graphics Inclusion
Version:        svn23739.v1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(keyval.sty)
Provides:       tex(rviewport.sty) = %{tl_version}

%description -n texlive-rviewport
Package graphicx provides a useful keyword viewport which
allows to show just a part of an image. However, one needs to
put there the actual coordinates of the viewport window.
Sometimes it is useful to have relative coordinates as
fractions of natural size. For example, one may want to print a
large image on a spread, putting a half on a verso page, and
another half on the next recto page. For this one would need a
viewport occupying exactly one half of the file's bounding box,
whatever the actual width of the image may be. This package
adds a new keyword rviewport to the graphicx package
specifiying Relative Viewport for graphics inclusion: a window
defined by the given fractions of the natural width and height
of the image.

%package -n texlive-rviewport-doc
Summary:        Documentation for rviewport
Version:        svn23739.v1.0

Provides:       tex-rviewport-doc
AutoReqProv:    No

%description -n texlive-rviewport-doc
Documentation for rviewport

%package -n texlive-sa-tikz
Provides:       tex-sa-tikz = %{tl_version}
License:        LPPL 1.3
Summary:        TikZ library to draw switching architectures
Version:        svn32815.0.7a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tikz.sty)
Provides:       tex(sa-tikz.sty) = %{tl_version}, tex(tikzlibraryswitching-architectures.code.tex) = %{tl_version}

%description -n texlive-sa-tikz
The package provides a library that offers an easy way to draw
switching architectures and to customize their aspect.

%package -n texlive-sa-tikz-doc
Summary:        Documentation for sa-tikz
Version:        svn32815.0.7a

Provides:       tex-sa-tikz-doc
AutoReqProv:    No

%description -n texlive-sa-tikz-doc
Documentation for sa-tikz

%package -n texlive-schemabloc
Provides:       tex-schemabloc = %{tl_version}
License:        LPPL
Summary:        Draw block diagrams, using Tikz
Version:        svn15878.1.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(tikz.sty)
Provides:       tex(schemabloc.sty) = %{tl_version}

%description -n texlive-schemabloc
The package provides a set of macros for constructing block
diagrams, using TikZ. (The blox package is an "English
translation" of this package.)

%package -n texlive-schemabloc-doc
Summary:        Documentation for schemabloc
Version:        svn15878.1.5

Provides:       tex-schemabloc-doc
AutoReqProv:    No

%description -n texlive-schemabloc-doc
Documentation for schemabloc

%package -n texlive-setdeck
Provides:       tex-setdeck = %{tl_version}
License:        GPLv3+
Summary:        Typeset cards for Set
Version:        svn40613

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xcolor.sty), tex(tikz.sty)
Provides:       tex(setdeck.sty) = %{tl_version}

%description -n texlive-setdeck
The package will typeset cards for use in a game of Set.

%package -n texlive-setdeck-doc
Summary:        Documentation for setdeck
Version:        svn40613

Provides:       tex-setdeck-doc
AutoReqProv:    No

%description -n texlive-setdeck-doc
Documentation for setdeck

%package -n texlive-sauerj
Provides:       tex-sauerj = %{tl_version}
License:        LPPL
Summary:        A bundle of utilities by Jonathan Sauer
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(keyval.sty)
Provides:       tex(collect.sty) = %{tl_version}, tex(metainfo.sty) = %{tl_version}
Provides:       tex(optparams.sty) = %{tl_version}, tex(parcolumns.sty) = %{tl_version}
Provides:       tex(processkv.sty) = %{tl_version}, tex(zahl2string.sty) = %{tl_version}

%description -n texlive-sauerj
The bundle consists of: a tool for collecting text for later re-
use, a tool for typesetting the "meta-information" within a
text, a tool for use in constructing macros with multiple
optional parameters, a package for multiple column parallel
texts, a tool for processing key-value structured lists, and
macros for typesetting a number as a German-language string.

%package -n texlive-sauerj-doc
Summary:        Documentation for sauerj
Version:        svn15878.0

Provides:       tex-sauerj-doc
AutoReqProv:    No

%description -n texlive-sauerj-doc
Documentation for sauerj

%package -n texlive-robustcommand
Provides:       tex-robustcommand = %{tl_version}
License:        LPPL
Summary:        Declare robust command, with \newcommand checks
Version:        svn15878.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(robustcommand.sty) = %{tl_version}

%description -n texlive-robustcommand
The package merely provides a variation of
\DeclareRobustCommand, which checks for the existence of a
command before declaring it robust.

%package -n texlive-robustcommand-doc
Summary:        Documentation for robustcommand
Version:        svn15878.0.1

Provides:       tex-robustcommand-doc
AutoReqProv:    No

%description -n texlive-robustcommand-doc
Documentation for robustcommand

%package -n texlive-robustindex
Provides:       tex-robustindex = %{tl_version}
License:        LPPL
Summary:        Create index with pagerefs
Version:        svn47521
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(robustglossary.sty) = %{tl_version}, tex(robustindex.sty) = %{tl_version}

%description -n texlive-robustindex
Third parties often change the page numbers without rerunning
makeindex. One would like to make the page numbers in the index
entries more robust. This bundle provides robustindex.sty and
robustglossary.sty, which use the \pageref mechanism to
maintain correct page numbers

%package -n texlive-robustindex-doc
Summary:        Documentation for robustindex
Version:        svn47521
Provides:       tex-robustindex-doc
AutoReqProv:    No

%description -n texlive-robustindex-doc
Documentation for robustindex

%package -n texlive-romanbar
Provides:       tex-romanbar = %{tl_version}
License:        LPPL 1.3
Summary:        Write roman number with "bars"
Version:        svn25005.1.0f

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(romanbar.sty) = %{tl_version}

%description -n texlive-romanbar
'Bars', in the present context, are lines above and below text
that abut with the text. Barred roman numerals are sometimes
found in publications. The package provides a function that
prints barred roman numerals (converting arabic numerals if
necessary). The package also provides a predicate \ifnumeric.

%package -n texlive-romanbar-doc
Summary:        Documentation for romanbar
Version:        svn25005.1.0f

Provides:       tex-romanbar-doc
AutoReqProv:    No

%description -n texlive-romanbar-doc
Documentation for romanbar

%package -n texlive-romanbarpagenumber
Provides:       tex-romanbarpagenumber = %{tl_version}
License:        LPPL 1.3
Summary:        Typesetting roman page numbers
Version:        svn36236.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(kvoptions.sty), tex(xifthen.sty), tex(romanbar.sty)
Provides:       tex(romanbarpagenumber.sty) = %{tl_version}

%description -n texlive-romanbarpagenumber
The package romanbar allows to typeset roman numbers with bars.
This package allows you to use those roman numbers as page
number.

%package -n texlive-romanbarpagenumber-doc
Summary:        Documentation for romanbarpagenumber
Version:        svn36236.1.0

Provides:       tex-romanbarpagenumber-doc
AutoReqProv:    No

%description -n texlive-romanbarpagenumber-doc
Documentation for romanbarpagenumber

%package -n texlive-romanneg
Provides:       tex-romanneg = %{tl_version}
License:        Public Domain
Summary:        Roman page numbers negative
Version:        svn20087.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(romanneg.sty) = %{tl_version}

%description -n texlive-romanneg
Causes the page numbers in the DVI file (as defined by \count0)
to be negative when roman pagenumbering is in effect.

%package -n texlive-romanneg-doc
Summary:        Documentation for romanneg
Version:        svn20087.0

Provides:       tex-romanneg-doc
AutoReqProv:    No

%description -n texlive-romanneg-doc
Documentation for romanneg

%package -n texlive-romannum
Provides:       tex-romannum = %{tl_version}
License:        LPPL
Summary:        Generate roman numerals instead of arabic digits
Version:        svn15878.1.0b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(stdclsdv.sty)
Provides:       tex(romannum.sty) = %{tl_version}

%description -n texlive-romannum
The romannum package changes LaTeX generated numbers to be
printed with roman numerals instead of arabic digits. It
requires the stdclsdv package. Users of the bookhands fonts may
find this package useful.

%package -n texlive-romannum-doc
Summary:        Documentation for romannum
Version:        svn15878.1.0b

Provides:       tex-romannum-doc
AutoReqProv:    No

%description -n texlive-romannum-doc
Documentation for romannum

%package -n texlive-rotfloat
Provides:       tex-rotfloat = %{tl_version}
License:        LPPL
Summary:        Rotate floats
Version:        svn18292.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(float.sty), tex(rotating.sty)
Provides:       tex(rotfloat.sty) = %{tl_version}

%description -n texlive-rotfloat
The float package provides commands to define new floats of
various styles (plain, boxed, ruled, and userdefined ones); the
rotating package provides new environments (sidewaysfigure and
sidewaystable) which are rotated by 90 or 270 degrees. But what
about new rotated floats, e.g. a rotated ruled one? This
package makes this possible; it builds a bridge between the two
packages and extends the commands from the float package to
define rotated versions of the new floats, too.

%package -n texlive-rotfloat-doc
Summary:        Documentation for rotfloat
Version:        svn18292.1.2

Provides:       tex-rotfloat-doc
AutoReqProv:    No

%description -n texlive-rotfloat-doc
Documentation for rotfloat

%package -n texlive-rotpages
Provides:       tex-rotpages = %{tl_version}
License:        LPPL
Summary:        Typeset sets of pages upside-down and backwards
Version:        svn18740.3.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphics.sty), tex(ifthen.sty), tex(calc.sty)
Provides:       tex(rotpages.sty) = %{tl_version}

%description -n texlive-rotpages
The rotpages package allows you to format documents where small
sets of pages are rotated by 180 degrees and rearranged, so
that they can be read by turning the printed copy upside-down.
It was developed for collecting exercises and solutions: using
the package, you can print the exercise text normally and the
solutions rotated.

%package -n texlive-rotpages-doc
Summary:        Documentation for rotpages
Version:        svn18740.3.0

Provides:       tex-rotpages-doc
AutoReqProv:    No

%description -n texlive-rotpages-doc
Documentation for rotpages

%package -n texlive-roundbox
Provides:       tex-roundbox = %{tl_version}
License:        LPPL 1.3
Summary:        Round boxes in LaTeX
Version:        svn29675.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(roundbox.sty) = %{tl_version}

%description -n texlive-roundbox
This package implements a command \roundbox that can be used,
in LaTeX, for producing boxes, framed with rounded corners.

%package -n texlive-roundbox-doc
Summary:        Documentation for roundbox
Version:        svn29675.0.2

Provides:       tex-roundbox-doc
AutoReqProv:    No

%description -n texlive-roundbox-doc
Documentation for roundbox

%package -n texlive-rterface
Provides:       tex-rterface = %{tl_version}
License:        LPPL 1.2
Summary:        Access to R analysis from within a document
Version:        svn30084.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(newfile.sty)
Provides:       tex(rterface.sty) = %{tl_version}

%description -n texlive-rterface
The package mediates interaction between LaTeX and R; it allows
LaTeX to set R's parameters, and provides code to read R
output.

%package -n texlive-rterface-doc
Summary:        Documentation for rterface
Version:        svn30084.0

Provides:       tex-rterface-doc
AutoReqProv:    No

%description -n texlive-rterface-doc
Documentation for rterface

%package -n texlive-rtkinenc
Provides:       tex-rtkinenc = %{tl_version}
License:        LPPL
Summary:        Input encoding with fallback procedures
Version:        svn20003.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(rtkinenc.sty) = %{tl_version}

%description -n texlive-rtkinenc
The rtkinenc package is functionally similar to the standard
LaTeX package inputenc: both set up active characters so that
an input character outside the range of 7-bit visible ASCII is
coverted into one or more corresponding LaTeX commands. The
main difference lies in that rtkinenc allows the user to
specify a fallback procedure to use when the text command
corresponding to some input character isn't available. Names of
commands in rtkinenc have been selected so that it can read
inputenc encoding definition files, and the aim is that
rtkinenc should be backwards compatible with inputenc. rtkinenc
is not a new version of inputenc though, nor is it part of
standard LaTeX. For an example of how rtkinenc is used, the
user may look at the tclldoc class.

%package -n texlive-rtkinenc-doc
Summary:        Documentation for rtkinenc
Version:        svn20003.1.0

Provides:       tex-rtkinenc-doc
AutoReqProv:    No

%description -n texlive-rtkinenc-doc
Documentation for rtkinenc

%package -n texlive-rrgtrees
Provides:       tex-rrgtrees = %{tl_version}
License:        LPPL
Summary:        Linguistic tree diagrams for Role and Reference Grammar (RRG) with LaTeX
Version:        svn27322.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pst-node.sty), tex(pst-tree.sty)
Provides:       tex(rrgtrees.sty) = %{tl_version}

%description -n texlive-rrgtrees
A set of LaTeX macros that makes it easy to produce linguistic
tree diagrams suitable for Role and Reference Grammar (RRG).
This package allows the construction of trees with crossing
lines, as is required by this theory for many languages. There
is no known limit on number of tree nodes or levels. Requires
the pst-node and pst-tree LaTeX packages.

%package -n texlive-rrgtrees-doc
Summary:        Documentation for rrgtrees
Version:        svn27322.1.1

Provides:       tex-rrgtrees-doc
AutoReqProv:    No

%description -n texlive-rrgtrees-doc
Documentation for rrgtrees

%package -n texlive-rtklage
Provides:       tex-rtklage = %{tl_version}
License:        LPPL
Summary:        A package for German lawyers
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(babel.sty), tex(twoopt.sty), tex(ifthen.sty), tex(scrdate.sty)
Requires:       tex(calc.sty), tex(numprint.sty), tex(scrpage2.sty), tex(alphanum.sty)
Requires:       tex(eso-pic.sty), tex(color.sty), tex(graphicx.sty), tex(xspace.sty)
Provides:       tex(rtklage.cls) = %{tl_version}

%description -n texlive-rtklage
RATeX is a newly developed bundle of packages and classes
provided for German lawyers. Now in the early beginning it only
contains rtklage, a class to make lawsuits.

%package -n texlive-rtklage-doc
Summary:        Documentation for rtklage
Version:        svn15878.0

Provides:       tex-rtklage-doc
AutoReqProv:    No

%description -n texlive-rtklage-doc
Documentation for rtklage

%package -n texlive-ruhyphen
Provides:       tex-ruhyphen = %{tl_version}
License:        LPPL
Summary:        Russian hyphenation
Version:        svn21081.1.6

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(catkoi.tex) = %{tl_version}, tex(cyryoal.tex) = %{tl_version}
Provides:       tex(cyryoas.tex) = %{tl_version}, tex(cyryoct.tex) = %{tl_version}
Provides:       tex(cyryodv.tex) = %{tl_version}, tex(cyryomg.tex) = %{tl_version}
Provides:       tex(cyryovl.tex) = %{tl_version}, tex(cyryozn.tex) = %{tl_version}
Provides:       tex(enrhm2.tex) = %{tl_version}, tex(hypht2.tex) = %{tl_version}
Provides:       tex(koi2koi.tex) = %{tl_version}, tex(koi2lcy.tex) = %{tl_version}
Provides:       tex(koi2ot2.tex) = %{tl_version}, tex(koi2t2a.tex) = %{tl_version}
Provides:       tex(koi2ucy.tex) = %{tl_version}, tex(ruenhyph.tex) = %{tl_version}
Provides:       tex(ruhyphal.tex) = %{tl_version}, tex(ruhyphas.tex) = %{tl_version}
Provides:       tex(ruhyphct.tex) = %{tl_version}, tex(ruhyphdv.tex) = %{tl_version}
Provides:       tex(ruhyphen.tex) = %{tl_version}, tex(ruhyphmg.tex) = %{tl_version}
Provides:       tex(ruhyphvl.tex) = %{tl_version}, tex(ruhyphzn.tex) = %{tl_version}

%description -n texlive-ruhyphen
A collection of Russian hyphenation patterns supporting a
number of Cyrillic font encodings, including T2, UCY (Omega
Unicode Cyrillic), LCY, LWN (OT2), and koi8-r.

%package -n texlive-roex
Provides:       tex-roex = %{tl_version}
License:        LPPL
Summary:        roex package
Version:        svn45818
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

%description -n texlive-roex
roex package

%package -n texlive-serbian-apostrophe
Provides:       tex-serbian-apostrophe = %{tl_version}
License:        LPPL 1.3
Summary:        Commands for Serbian words with apostrophes
Version:        svn23799.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xspace.sty), tex(tipa.sty)
Provides:       tex(serbian-apostrophe.sty) = %{tl_version}

%description -n texlive-serbian-apostrophe
The package provides a collection of commands (whose names are
Serbian words) whose expansion is the Serbian word with
appropriate apostrophes.

%package -n texlive-serbian-apostrophe-doc
Summary:        Documentation for serbian-apostrophe
Version:        svn23799.0

Provides:       tex-serbian-apostrophe-doc
AutoReqProv:    No

%description -n texlive-serbian-apostrophe-doc
Documentation for serbian-apostrophe

%package -n texlive-serbian-date-lat
Provides:       tex-serbian-date-lat = %{tl_version}
License:        GPLv2+
Summary:        Updated date typesetting for Serbian
Version:        svn23446.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(serbian-date-lat.sty) = %{tl_version}

%description -n texlive-serbian-date-lat
Babel defines dates for Serbian texts, in Latin script. The
style it uses does not match current practices. The present
package defines a \date command that solves the problem.

%package -n texlive-serbian-date-lat-doc
Summary:        Documentation for serbian-date-lat
Version:        svn23446.0

Provides:       tex-serbian-date-lat-doc
AutoReqProv:    No

%description -n texlive-serbian-date-lat-doc
Documentation for serbian-date-lat

%package -n texlive-serbian-def-cyr
Provides:       tex-serbian-def-cyr = %{tl_version}
License:        LPPL 1.3
Summary:        Serbian cyrillic localization
Version:        svn23734.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(inputenc.sty), tex(fontenc.sty)
Provides:       tex(serbian-def-cyr.sty) = %{tl_version}

%description -n texlive-serbian-def-cyr
This package provides abstract, chapter, title, date etc, for
serbian language in cyrillic scripts in T2A encoding and cp1251
code pages.

%package -n texlive-serbian-def-cyr-doc
Summary:        Documentation for serbian-def-cyr
Version:        svn23734.0

Provides:       tex-serbian-def-cyr-doc
AutoReqProv:    No

%description -n texlive-serbian-def-cyr-doc
Documentation for serbian-def-cyr

%package -n texlive-serbian-lig
Provides:       tex-serbian-lig = %{tl_version}
License:        LPPL 1.3
Summary:        Control ligatures in Serbian
Version:        svn48197
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xspace.sty)
Provides:       tex(serbian-lig.sty) = %{tl_version}

%description -n texlive-serbian-lig
The package suppresses fi and fl (and other ligatures) in
Serbian text written using Roman script.

%package -n texlive-serbian-lig-doc
Summary:        Documentation for serbian-lig
Version:        svn48197
Provides:       tex-serbian-lig-doc
AutoReqProv:    No

%description -n texlive-serbian-lig-doc
Documentation for serbian-lig

%package -n texlive-roundrect
Provides:       tex-roundrect = %{tl_version}
License:        LPPL 1.3
Summary:        Metapost macros for highly configurable rounded rectangles (optionally with text)
Version:        svn39796

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-roundrect
The roundrect macros for Metapost provide ways to produce
rounded rectangles, which may or may not contain a title bar or
text (the title bar may itself contain text). They are
extremely configurable.

%package -n texlive-roundrect-doc
Summary:        Documentation for roundrect
Version:        svn39796

Provides:       tex-roundrect-doc
AutoReqProv:    No

%description -n texlive-roundrect-doc
Documentation for roundrect

%package -n texlive-rulercompass
Provides:       tex-rulercompass = %{tl_version}
License:        LPPL 1.3
Summary:        A TikZ library for straight-edge and compass diagrams
Version:        svn32392.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(tikzlibraryrulercompass.code.tex) = %{tl_version}

%description -n texlive-rulercompass
The package defines some commands and styles to support drawing
straight-edge and compass diagrams with TikZ.

%package -n texlive-rulercompass-doc
Summary:        Documentation for rulercompass
Version:        svn32392.1

Provides:       tex-rulercompass-doc
AutoReqProv:    No

%description -n texlive-rulercompass-doc
Documentation for rulercompass

%package -n texlive-rvwrite
Provides:       tex-rvwrite = %{tl_version}
License:        LPPL
Summary:        Increase the number of available output streams in LaTeX
Version:        svn19614.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(rvwrite.sty) = %{tl_version}

%description -n texlive-rvwrite
The package addresses, for LaTeX documents, the severe
limitation on the number of output streams that TeX provides.
The package uses a single TeX output stream, and writes "marked-
up" output to this stream. The user may then post-process the
marked-up output file, using LaTeX, and the document's output
appears as separate files, according to the calls made to the
package. The output to be post-processed uses macros from the
widely-available ProTeX package.

%package -n texlive-rvwrite-doc
Summary:        Documentation for rvwrite
Version:        svn19614.1.2

Provides:       tex-rvwrite-doc
AutoReqProv:    No

%description -n texlive-rvwrite-doc
Documentation for rvwrite

%package -n texlive-r_und_s
Provides:       tex-r_und_s = %{tl_version}
License:        BSD
Summary:        Chemical hazard codes
Version:        svn15878.1.3i

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(eng_rs.sty) = %{tl_version}, tex(eng_rs.tex) = %{tl_version}
Provides:       tex(fr_rs.sty) = %{tl_version}, tex(fr_rs.tex) = %{tl_version}
Provides:       tex(nl_rs.sty) = %{tl_version}, tex(nl_rs.tex) = %{tl_version}
Provides:       tex(r_und_s.sty) = %{tl_version}, tex(r_und_s.tex) = %{tl_version}

%description -n texlive-r_und_s
The r_und_s package decodes the german 'R- und S-Satze', which
are numerically coded security advice for chemical substances
into plain text. This is, e.g., used to compose security sheets
or lab protocols and especially useful for students of
chemistry. There are four packages, giving texts in German,
English, French and Dutch.

%package -n texlive-r_und_s-doc
Summary:        Documentation for r_und_s
Version:        svn15878.1.3i

Provides:       tex-r_und_s-doc
AutoReqProv:    No

%description -n texlive-r_und_s-doc
Documentation for r_und_s

%package -n texlive-savefnmark
Provides:       tex-savefnmark = %{tl_version}
License:        GPL+
Summary:        Save name of the footnote mark for reuse
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(savefnmark.sty) = %{tl_version}

%description -n texlive-savefnmark
Sometimes the same footnote applies to more than one location
in a table. With this package the mark of a footnote can be
saved into a name, and re-used subsequently without creating
another footnote at the bottom.

%package -n texlive-savefnmark-doc
Summary:        Documentation for savefnmark
Version:        svn15878.1.0

Provides:       tex-savefnmark-doc
AutoReqProv:    No

%description -n texlive-savefnmark-doc
Documentation for savefnmark

%package -n texlive-savesym
Provides:       tex-savesym = %{tl_version}
License:        LPPL
Summary:        Redefine symbols where names conflict
Version:        svn31565.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(savesym.sty) = %{tl_version}

%description -n texlive-savesym
There are a number of symbols (e.g., \Square) that are defined
by several packages. In order to typeset all the variants in a
document, we have to give the glyph a unique name. To do that,
we define \savesymbol{XXX}, which renames a symbol from \XXX to
\origXXX, and \restoresymbols{yyy}{XXX}, which renames \origXXX
back to \XXX and defines a new command, \yyyXXX, which
corresponds to the most recently loaded version of \XXX.

%package -n texlive-savetrees
Provides:       tex-savetrees = %{tl_version}
License:        LPPL 1.3
Summary:        Optimise the use of each page of a LaTeX document
Version:        svn40525

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(numeric-comp.bbx), tex(numeric-comp.cbx)
Requires:       tex(xkeyval.sty), tex(ifpdf.sty), tex(ifluatex.sty), tex(titlesec.sty)
Provides:       tex(savetrees.bbx) = %{tl_version}, tex(savetrees.cbx) = %{tl_version}
Provides:       tex(savetrees.sty) = %{tl_version}

%description -n texlive-savetrees
The goal of the savetrees package is to pack as much text as
possible onto each page of a LaTeX document. Admittedly, this
makes the document far less attractive. Nevertheless, savetrees
is a simple way to save paper when printing draft copies of a
document. It can also be useful when trying to meet a tight
page-length requirement for a conference or journal submission.
Most of the package options cover specific modifications to
typesetting rules, but there are also options subtle, moderate
and extreme options for the "broad brush" approach.

%package -n texlive-savetrees-doc
Summary:        Documentation for savetrees
Version:        svn40525

Provides:       tex-savetrees-doc
AutoReqProv:    No

%description -n texlive-savetrees-doc
Documentation for savetrees

%package -n texlive-scale
Provides:       tex-scale = %{tl_version}
License:        GPL+
Summary:        Scale document by sqrt(2) or magstep(2)
Version:        svn15878.1.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(scale.sty) = %{tl_version}

%description -n texlive-scale
A package to scale a document by sqrt(2) (or by \magstep{2}).
This is useful if you are preparing a document on, for example,
A5 paper and want to print on A4 paper to achieve a better
resolution.

%package -n texlive-scale-doc
Summary:        Documentation for scale
Version:        svn15878.1.1.2

Provides:       tex-scale-doc
AutoReqProv:    No

%description -n texlive-scale-doc
Documentation for scale

%package -n texlive-scalebar
Provides:       tex-scalebar = %{tl_version}
License:        LPPL
Summary:        Create scalebars for maps, diagrams or photos
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(calc.sty), tex(fp.sty)
Provides:       tex(scalebar.sty) = %{tl_version}

%description -n texlive-scalebar
This is a small package to create scalebars for maps, diagrams
or photos. It was designed for use with cave maps but can be
used for anything from showing a scalebar in kilometres for
topographic maps to a scalebar in micrometres for an electron
microscope image.

%package -n texlive-scalebar-doc
Summary:        Documentation for scalebar
Version:        svn15878.1.0

Provides:       tex-scalebar-doc
AutoReqProv:    No

%description -n texlive-scalebar-doc
Documentation for scalebar

%package -n texlive-scalerel
Provides:       tex-scalerel = %{tl_version}
License:        LPPL 1.3
Summary:        Constrained scaling and stretching of objects
Version:        svn42809
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(scalerel.sty) = %{tl_version}

%description -n texlive-scalerel
The package provides four commands for vertically scaling and
stretching objects. Its primary function is the ability to
scale/stretch and shift one object to conform to the size of a
specified second object. This feature can be useful in both
equations and schematic diagrams. Additionally, the scaling and
stretching commands offer constraints on maximum width and/or
minimum aspect ratio, which are often used to preserve
legibility or for the sake of general appearance.

%package -n texlive-scalerel-doc
Summary:        Documentation for scalerel
Version:        svn42809
Provides:       tex-scalerel-doc
AutoReqProv:    No

%description -n texlive-scalerel-doc
Documentation for scalerel

%package -n texlive-scanpages
Provides:       tex-scanpages = %{tl_version}
License:        LPPL 1.3
Summary:        Support importing and embellishing scanned documents
Version:        svn42633
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifpdf.sty), tex(pgffor.sty), tex(xcolor.sty), tex(xkeyval.sty)
Requires:       tex(fp-basic.sty), tex(graphicx.sty), tex(etoolbox.sty)
Provides:       tex(scanpages.sty) = %{tl_version}

%description -n texlive-scanpages
The bundle provides support for the process of creating
documents based on pre-TeX-era material that is available as
scanned pages, only.

%package -n texlive-scanpages-doc
Summary:        Documentation for scanpages
Version:        svn42633
Provides:       tex-scanpages-doc
AutoReqProv:    No

%description -n texlive-scanpages-doc
Documentation for scanpages

%package -n texlive-sdrt
Provides:       tex-sdrt = %{tl_version}
License:        LPPL
Summary:        Macros for Segmented Discourse Representation Theory
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(xyling.sty), tex(xytree.sty)
Provides:       tex(sdrt.sty) = %{tl_version}

%description -n texlive-sdrt
The package provides macros to produce the 'Box notation' of
SDRT (and DRT), to draw trees representing discourse relations,
and finally to have an easy access to various mathematical
symbols used in that theory, mostly with automatic mathematics
mode, so they work the same in formulae and in text.

%package -n texlive-sdrt-doc
Summary:        Documentation for sdrt
Version:        svn15878.1.0

Provides:       tex-sdrt-doc
AutoReqProv:    No

%description -n texlive-sdrt-doc
Documentation for sdrt

%package -n texlive-secdot
Provides:       tex-secdot = %{tl_version}
License:        LPPL
Summary:        Section numbers with trailing dots
Version:        svn20208.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(secdot.sty) = %{tl_version}

%description -n texlive-secdot
Makes the numbers of \section commands come out with a trailing
dot. Includes a command whereby the same can be made to happen
with other sectioning commands.

%package -n texlive-secdot-doc
Summary:        Documentation for secdot
Version:        svn20208.1.0

Provides:       tex-secdot-doc
AutoReqProv:    No

%description -n texlive-secdot-doc
Documentation for secdot

%package -n texlive-sectionbox
Provides:       tex-sectionbox = %{tl_version}
License:        LPPL
Summary:        Create fancy boxed ((sub)sub)sections
Version:        svn37749.1.01

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(calc.sty), tex(fancybox.sty), tex(color.sty)
Provides:       tex(sectionbox.sty) = %{tl_version}

%description -n texlive-sectionbox
Sectionbox is a LaTeX package for putting fancy colored boxes
around sections, subsections, and subsubsections, especially
for use in posters, etc. It was designed with the sciposter
class in mind, and certainly works with that class and with
derived classes.

%package -n texlive-sectionbox-doc
Summary:        Documentation for sectionbox
Version:        svn37749.1.01

Provides:       tex-sectionbox-doc
AutoReqProv:    No

%description -n texlive-sectionbox-doc
Documentation for sectionbox

%package -n texlive-sectsty
Provides:       tex-sectsty = %{tl_version}
License:        LPPL
Summary:        Control sectional headers
Version:        svn15878.2.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(sectsty.sty) = %{tl_version}

%description -n texlive-sectsty
A LaTeX2e package to help change the style of any or all of
LaTeX's sectional headers in the article, book, or report
classes. Examples include the addition of rules above or below
a section title.

%package -n texlive-sectsty-doc
Summary:        Documentation for sectsty
Version:        svn15878.2.0.2

Provides:       tex-sectsty-doc
AutoReqProv:    No

%description -n texlive-sectsty-doc
Documentation for sectsty

%package -n texlive-seealso
Provides:       tex-seealso = %{tl_version}
License:        LPPL 1.3
Summary:        Improve the performance of \see macros with makeindex
Version:        svn43595
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(etoolbox.sty), tex(kvoptions.sty)
Provides:       tex(seealso.sty) = %{tl_version}

%description -n texlive-seealso
The package amends the \see and \seealso macros that are used
in building indexes with makeindex, to deal with repetitions,
and to ensure page numbers are present in the actual index
entries. on these indirecty

%package -n texlive-seealso-doc
Summary:        Documentation for seealso
Version:        svn43595
Provides:       tex-seealso-doc
AutoReqProv:    No

%description -n texlive-seealso-doc
Documentation for seealso

%package -n texlive-selectp
Provides:       tex-selectp = %{tl_version}
License:        Public Domain
Summary:        Select pages to be output
Version:        svn20185.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(selectp.sty) = %{tl_version}

%description -n texlive-selectp
Defines a command \outputonly, whose argument is a list of
pages to be output. With the command present (before
\begin{document}), only those pages are output. This package
was inspired by code published by Knuth in TUGboat 8(2) (July
1987).

%package -n texlive-selectp-doc
Summary:        Documentation for selectp
Version:        svn20185.1.0

Provides:       tex-selectp-doc
AutoReqProv:    No

%description -n texlive-selectp-doc
Documentation for selectp

%package -n texlive-selnolig
Provides:       tex-selnolig = %{tl_version}
License:        LPPL 1.3
Summary:        Selectively disable typographic ligatures
Version:        svn38721

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifluatex.sty), tex(luatexbase.sty)
Provides:       tex(selnolig-english-hyphex.sty) = %{tl_version}
Provides:       tex(selnolig-english-patterns.sty) = %{tl_version}
Provides:       tex(selnolig-german-hyphex.sty) = %{tl_version}
Provides:       tex(selnolig-german-patterns.sty) = %{tl_version}
Provides:       tex(selnolig.sty) = %{tl_version}

%description -n texlive-selnolig
The package suppresses typographic ligatures selectively, i.e.,
based on predefined search patterns. The search patterns focus
on ligatures deemed inappropriate because they span morpheme
boundaries. For example, the word shelfful, which is mentioned
in the TeXbook as a word for which the ff ligature might be
inappropriate, is automatically typeset as shelf\/ful rather
than as shel{ff}ul. For English and German language documents,
the package provides extensive rules for the selective
suppression of so-called "common" ligatures. These comprise the
ff, fi, fl, ffi, and ffl ligatures as well as the ft and fft
ligatures. Other f-ligatures, such as fb, fh, fj and fk, are
suppressed globally, while exceptions are made for names and
words of non-English/German origin, such as Kafka and fjord.
For English language documents, the package further provides
ligature suppression macros for a number of so-called
"discretionary" or "rare" ligatures such as ct, st, and sp. The
package requires use of a recent LuaLaTeX format (for example
those from TeX Live 2012 or 2013, or MiKTeX 2.9).

%package -n texlive-selnolig-doc
Summary:        Documentation for selnolig
Version:        svn38721

Provides:       tex-selnolig-doc
AutoReqProv:    No

%description -n texlive-selnolig-doc
Documentation for selnolig

%package -n texlive-semantic
Provides:       tex-semantic = %{tl_version}
License:        LPPL
Summary:        Help for writing programming language semantics
Version:        svn15878.2.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(mathbbol.sty)
Provides:       tex(infernce.sty) = %{tl_version}, tex(ligature.sty) = %{tl_version}
Provides:       tex(reserved.sty) = %{tl_version}, tex(semantic.sty) = %{tl_version}
Provides:       tex(shrthand.sty) = %{tl_version}, tex(tdiagram.sty) = %{tl_version}

%description -n texlive-semantic
Eases the typesetting of notation of semantics and compilers.
Includes T-diagrams, various derivation symbols and inference
trees.

%package -n texlive-semantic-doc
Summary:        Documentation for semantic
Version:        svn15878.2.0

Provides:       tex-semantic-doc
AutoReqProv:    No

%description -n texlive-semantic-doc
Documentation for semantic

%package -n texlive-semioneside
Provides:       tex-semioneside = %{tl_version}
License:        LPPL
Summary:        Put only special contents on left-hand pages in two sided layout
Version:        svn15878.v0.41

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(afterpage.sty)
Provides:       tex(semioneside.sty) = %{tl_version}

%description -n texlive-semioneside
This package supports the preparation of semi one sided
documents. That is, two sided documents, where all text is
output on right-hand pages--as in a one-sided documents--and
only special contents are output on left-hand pages on user
request, e.g., floating objects.

%package -n texlive-semioneside-doc
Summary:        Documentation for semioneside
Version:        svn15878.v0.41

Provides:       tex-semioneside-doc
AutoReqProv:    No

%description -n texlive-semioneside-doc
Documentation for semioneside

%package -n texlive-semproc
Provides:       tex-semproc = %{tl_version}
License:        LPPL 1.3
Summary:        Seminar proceedings
Version:        svn37568.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xkeyval.sty), tex(xcolor.sty), tex(etoc.sty), tex(hyperref.sty)
Requires:       tex(bookmark.sty), tex(etoolbox.sty), tex(biblatex.sty), tex(csquotes.sty)
Provides:       tex(semproc.cls) = %{tl_version}

%description -n texlive-semproc
The package provides functionality for typesetting seminar
proceedings based on KOMA-Script's scrreprt class and etoc. It
offers an alternative to \chapter that typesets the speaker and
if necessary the typist of the notes for the talk in question.
Moreover, the class provides two types of table of contents. A
global table of contents showing only the talks of the seminar
and the respective speakers and a local table of contents for
each talk showing the sections and subsections of the
respective talk.

%package -n texlive-semproc-doc
Summary:        Documentation for semproc
Version:        svn37568.0.1

Provides:       tex-semproc-doc
AutoReqProv:    No

%description -n texlive-semproc-doc
Documentation for semproc

%package -n texlive-sepfootnotes
Provides:       tex-sepfootnotes = %{tl_version}
License:        LPPL 1.3
Summary:        Support footnotes and endnotes from separate files
Version:        svn41732
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(sepfootnotes.sty) = %{tl_version}

%description -n texlive-sepfootnotes
The package supports footnotes and endnotes from separate
files. This is achieved with commands \sepfootnotecontent and
\sepfootnote; the former defines the content of a note, while
the latter typesets that note.

%package -n texlive-sepfootnotes-doc
Summary:        Documentation for sepfootnotes
Version:        svn41732
Provides:       tex-sepfootnotes-doc
AutoReqProv:    No

%description -n texlive-sepfootnotes-doc
Documentation for sepfootnotes

%package -n texlive-seqsplit
Provides:       tex-seqsplit = %{tl_version}
License:        LPPL
Summary:        Split long sequences of characters in a neutral way
Version:        svn15878.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(seqsplit.sty) = %{tl_version}

%description -n texlive-seqsplit
When one needs to type long sequences of letters (such as in
base-sequences in genes) or of numbers (such as calculations of
transcendental numbers), there's no obvious break points to be
found. The package provides a command \seqsplit, which makes
its argument splittable anywhere, and then leaves the TeX
paragraph-maker to do the splitting. While the package may
obviously be used to typeset DNA sequences, the user may
consider the dnaseq as a rather more powerful alternative.

%package -n texlive-seqsplit-doc
Summary:        Documentation for seqsplit
Version:        svn15878.0.1

Provides:       tex-seqsplit-doc
AutoReqProv:    No

%description -n texlive-seqsplit-doc
Documentation for seqsplit

%package -n texlive-sf298
Provides:       tex-sf298 = %{tl_version}
License:        LPPL
Summary:        Standard form 298
Version:        svn41653
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(sf298.sty) = %{tl_version}

%description -n texlive-sf298
A LaTeX package for generating a completed standard form 298
(Rev. 8-98) as prescribed by ANSI Std. Z39.18 for report
documentation as part of a document delivered, for instance, on
a U.S. government contract.

%package -n texlive-sf298-doc
Summary:        Documentation for sf298
Version:        svn41653
Provides:       tex-sf298-doc
AutoReqProv:    No

%description -n texlive-sf298-doc
Documentation for sf298

%package -n texlive-sffms
Provides:       tex-sffms = %{tl_version}
License:        LPPL
Summary:        Typesetting science fiction/fantasy manuscripts
Version:        svn15878.2.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fontenc.sty), tex(fancyhdr.sty), tex(ulem.sty), tex(setspace.sty)
Requires:       tex(geometry.sty)
Provides:       tex(sffdumb.sty) = %{tl_version}, tex(sffms.cls) = %{tl_version}
Provides:       tex(sffsmart.sty) = %{tl_version}

%description -n texlive-sffms
The class is designed for typesetting science fiction and
fantasy manuscripts. Sffms now includes several options for
specific publishers as well as extensive documentation aimed at
new LaTeX users.

%package -n texlive-sffms-doc
Summary:        Documentation for sffms
Version:        svn15878.2.0

Provides:       tex-sffms-doc
AutoReqProv:    No

%description -n texlive-sffms-doc
Documentation for sffms

%package -n texlive-sfmath
Provides:       tex-sfmath = %{tl_version}
License:        LPPL
Summary:        Sans-serif mathematics
Version:        svn15878.0.8

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(sfmath.sty) = %{tl_version}

%description -n texlive-sfmath
sfmath is a simple package for sans serif maths in documents.
After including the package, all maths of the current document
is displayed with sans serif fonts.

%package -n texlive-sesamanuel
Provides:       tex-sesamanuel = %{tl_version}
License:        LPPL 1.3
Summary:        Class and package for sesamath books or paper
Version:        svn36613.0.6

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etex.sty), tex(fontspec.sty), tex(xunicode.sty), tex(fontenc.sty)
Requires:       tex(inputenc.sty), tex(helvet.sty), tex(mathpazo.sty), tex(mathrsfs.sty)
Requires:       tex(pifont.sty), tex(eurosym.sty), tex(geometry.sty), tex(crop.sty)
Requires:       tex(ifmtarg.sty), tex(mathtools.sty), tex(amssymb.sty), tex(longtable.sty)
Requires:       tex(tabularx.sty), tex(multirow.sty), tex(xcolor.sty), tex(pst-all.sty)
Requires:       tex(pstricks-add.sty), tex(fancyhdr.sty)
Requires:       tex(fancyvrb.sty), tex(multicol.sty), tex(babel.sty), tex(numprint.sty)
Requires:       tex(colortbl.sty), tex(multido.sty), tex(esvect.sty), tex(tikz.sty)
Requires:       tex(tkz-tab.sty), tex(pgf.sty)
Provides:       tex(sesamanuel.cls) = %{tl_version}, tex(sesamanuel.sty) = %{tl_version}
Provides:       tex(sesamanuelTIKZ.sty) = %{tl_version}

%description -n texlive-sesamanuel
The package contains a sesamanuel class which could be used to
compose a student's classroom book with LaTeX, and also a
sesamanuelTIKZ style to be used for TIKZ pictures in the
sesamath book.

%package -n texlive-sesamanuel-doc
Summary:        Documentation for sesamanuel
Version:        svn36613.0.6

Provides:       tex-sesamanuel-doc
AutoReqProv:    No

%description -n texlive-sesamanuel-doc
Documentation for sesamanuel

%package -n texlive-ryethesis
Provides:       tex-ryethesis = %{tl_version}
License:        LPPL 1.3
Summary:        Class for Ryerson Unversity Graduate School requirements
Version:        svn33945.1.36

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(fancyhdr.sty), tex(setspace.sty), tex(vmargin.sty)
Requires:       tex(float.sty), tex(hyperref.sty), tex(bookmark.sty), tex(glossaries.sty)
Requires:       tex(multicol.sty), tex(nomencl.sty), tex(etoolbox.sty)
Provides:       tex(ryethesis.cls) = %{tl_version}

%description -n texlive-ryethesis
The class offers support for formatting a thesis, dissertation
or project according to Ryerson University's School of Graduate
Studies thesis formatting regulations.

%package -n texlive-ryethesis-doc
Summary:        Documentation for ryethesis
Version:        svn33945.1.36

Provides:       tex-ryethesis-doc
AutoReqProv:    No

%description -n texlive-ryethesis-doc
Documentation for ryethesis

%package -n texlive-sageep
Provides:       tex-sageep = %{tl_version}
License:        LPPL
Summary:        Format papers for the annual meeting of EEGS
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(geometry.sty), tex(indentfirst.sty), tex(caption.sty), tex(natbib.sty)
Provides:       tex(sageep.cls) = %{tl_version}

%description -n texlive-sageep
The class provides formatting for papers for the annual meeting
of the Environmental and Engineering Geophysical Society (EEGS)
("Application of Geophysics to Engineering and Environmental
Problems", known as SAGEEP).

%package -n texlive-sageep-doc
Summary:        Documentation for sageep
Version:        svn15878.1.0

Provides:       tex-sageep-doc
AutoReqProv:    No

%description -n texlive-sageep-doc
Documentation for sageep

%package -n texlive-sapthesis
Provides:       tex-sapthesis = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset theses for Sapienza-University, Rome
Version:        svn48365
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xkeyval.sty), tex(geometry.sty), tex(ifxetex.sty), tex(xltxtra.sty)
Requires:       tex(fontenc.sty), tex(textcomp.sty), tex(lmodern.sty), tex(caption.sty)
Requires:       tex(graphicx.sty), tex(color.sty), tex(booktabs.sty), tex(amsmath.sty)
Requires:       tex(fancyhdr.sty)
Provides:       tex(sapthesis.cls) = %{tl_version}

%description -n texlive-sapthesis
The class will typeset Ph.D., Master, and Bachelor theses that
adhere to the publishing guidelines of the Sapienza-University
of Rome.

%package -n texlive-sapthesis-doc
Summary:        Documentation for sapthesis
Version:        svn48365
Provides:       tex-sapthesis-doc
AutoReqProv:    No

%description -n texlive-sapthesis-doc
Documentation for sapthesis

%package -n texlive-scrjrnl
Provides:       tex-scrjrnl = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset diaries or journals
Version:        svn27810.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(titlesec.sty), tex(datetime.sty), tex(fancytabs.sty)
Provides:       tex(scrjrnl.cls) = %{tl_version}

%description -n texlive-scrjrnl
A class, based on scrbook, designed for typesetting diaries,
journals or devotionals.

%package -n texlive-scrjrnl-doc
Summary:        Documentation for scrjrnl
Version:        svn27810.0.1

Provides:       tex-scrjrnl-doc
AutoReqProv:    No

%description -n texlive-scrjrnl-doc
Documentation for scrjrnl

%package -n texlive-schule
Provides:       tex-schule = %{tl_version}
License:        LPPL 1.3
Summary:        Support for teachers at German schools
Version:        svn37277.0.6

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tikz.sty), tex(circuitikz.sty), tex(etex.sty), tex(babel.sty)
Requires:       tex(ifthen.sty), tex(xifthen.sty), tex(xspace.sty), tex(tabularx.sty)
Requires:       tex(rotating.sty), tex(ragged2e.sty), tex(amssymb.sty), tex(amsmath.sty)
Requires:       tex(graphicx.sty), tex(paralist.sty), tex(textcomp.sty), tex(xmpincl.sty)
Requires:       tex(wrapfig.sty), tex(eurosym.sty), tex(multirow.sty), tex(multicol.sty)
Requires:       tex(ccicons.sty), tex(svn-multi.sty), tex(cancel.sty), tex(csquotes.sty)
Requires:       tex(inputenc.sty), tex(fontenc.sty), tex(scrpage2.sty), tex(mdframed.sty)
Requires:       tex(xargs.sty), tex(xparse.sty), tex(schulekl.sty), tex(calc.sty)
Requires:       tex(hyperref.sty), tex(adjustbox.sty), tex(pdfpages.sty), tex(geometry.sty)
Requires:       tex(natbib.sty), tex(biblatex.sty), tex(pgf-umlcd.sty), tex(listings.sty)
Requires:       tex(pgf-umlsd.sty), tex(struktex.sty), tex(units.sty), tex(mhchem.sty)
Provides:       tex(relaycircuit.sty) = %{tl_version}, tex(schule.sty) = %{tl_version}
Provides:       tex(schuleab.cls) = %{tl_version}, tex(schulein.cls) = %{tl_version}
Provides:       tex(schuleit.cls) = %{tl_version}, tex(schulekl.cls) = %{tl_version}
Provides:       tex(schulekl.sty) = %{tl_version}, tex(schuleub.cls) = %{tl_version}
Provides:       tex(schuleue.cls) = %{tl_version}, tex(schulinf.sty) = %{tl_version}
Provides:       tex(schullsg.cls) = %{tl_version}, tex(schullzk.cls) = %{tl_version}
Provides:       tex(schullzk.sty) = %{tl_version}, tex(schulphy.sty) = %{tl_version}
Provides:       tex(syntaxdi.sty) = %{tl_version}

%description -n texlive-schule
The 'schule' bundle was built to provide packages and commands
that could be useful for documents in German schools. At the
moment its main focus lies on documents for informatics as a
school subject. An extension for physics is currently in
progress. Extensions for other subjects are welcome. For the
time being, the whole package splits up into individual
packages for informatics (including syntax diagrams, Nassi-
Shneiderman diagrams, sequence diagrams, object diagrams, and
class diagrams) as well as classes for written exams (tests,
quizzes, teaching observations, information sheets, worksheets,
and answer keys).

%package -n texlive-schule-doc
Summary:        Documentation for schule
Version:        svn37277.0.6

Provides:       tex-schule-doc
AutoReqProv:    No

%description -n texlive-schule-doc
Documentation for schule

%package -n texlive-sduthesis
Provides:       tex-sduthesis = %{tl_version}
License:        LPPL 1.3
Summary:        Thesis Template of Shandong University
Version:        svn41401

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(kvoptions.sty), tex(etoolbox.sty), tex(ifpdf.sty), tex(ifxetex.sty)
Requires:       tex(geometry.sty), tex(amsmath.sty), tex(amsfonts.sty), tex(amsthm.sty)
Requires:       tex(amssymb.sty), tex(amsbsy.sty), tex(bm.sty), tex(mathrsfs.sty)
Requires:       tex(booktabs.sty), tex(graphicx.sty), tex(epstopdf.sty), tex(bmpsize.sty)
Requires:       tex(xcolor.sty), tex(makecell.sty)
Provides:       tex(sduthesis-cover.def) = %{tl_version}
Provides:       tex(sduthesis-statement.def) = %{tl_version}
Provides:       tex(sduthesis.cls) = %{tl_version}

%description -n texlive-sduthesis
Thesis Template of Shandong University.

%package -n texlive-sduthesis-doc
Summary:        Documentation for sduthesis
Version:        svn41401

Provides:       tex-sduthesis-doc
AutoReqProv:    No

%description -n texlive-sduthesis-doc
Documentation for sduthesis

%package -n texlive-seuthesis
Provides:       tex-seuthesis = %{tl_version}
License:        GPLv3+
Summary:        LaTeX template for theses at Southeastern University
Version:        svn33042.2.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-seuthesis
This template is for theses at Southeastern University,
Nanjing, China.

%package -n texlive-seuthesis-doc
Summary:        Documentation for seuthesis
Version:        svn33042.2.1.2

Provides:       tex-seuthesis-doc
AutoReqProv:    No

%description -n texlive-seuthesis-doc
Documentation for seuthesis

%package -n texlive-sasnrdisplay
Provides:       tex-sasnrdisplay = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset SAS or R code or output
Version:        svn45963
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(listings.sty), tex(xkeyval.sty), tex(xcolor.sty), tex(etoolbox.sty)
Requires:       tex(caption.sty), tex(needspace.sty)
Provides:       tex(SASnRdisplay.cfg) = %{tl_version}, tex(SASnRdisplay.sty) = %{tl_version}

%description -n texlive-sasnrdisplay
The SASnRdisplay package serves as a front-end to the listings,
which permits statisticians and others to import source code,
and the results of their calculations or simulations into LaTeX
projects. The package is also capable of overloading the Sweave
and SASweave packages.

%package -n texlive-sasnrdisplay-doc
Summary:        Documentation for sasnrdisplay
Version:        svn45963
Provides:       tex-sasnrdisplay-doc
AutoReqProv:    No

%description -n texlive-sasnrdisplay-doc
Documentation for sasnrdisplay

%package -n texlive-sciposter
Provides:       tex-sciposter = %{tl_version}
License:        LPPL
Summary:        Make posters of ISO A3 size and larger
Version:        svn15878.1.18

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(lettrine.sty), tex(graphics.sty), tex(color.sty)
Requires:       tex(shadow.sty), tex(a0size.sty), tex(times.sty), tex(boxedminipage.sty)
Provides:       tex(paperb0.cfg) = %{tl_version}, tex(paperb1.cfg) = %{tl_version}
Provides:       tex(paperb2.cfg) = %{tl_version}, tex(paperb3.cfg) = %{tl_version}
Provides:       tex(papercustom.cfg) = %{tl_version}, tex(paperra0.cfg) = %{tl_version}
Provides:       tex(paperra1.cfg) = %{tl_version}, tex(paperra2.cfg) = %{tl_version}
Provides:       tex(sciposter.cls) = %{tl_version}

%description -n texlive-sciposter
This collection of files contains LaTeX packages for posters of
ISO A3 size and larger (ISO A0 is the default size). American
paper sizes and custom paper are supported. In particular,
sciposter.cls defines a document class which allows cutting and
pasting most of an article to a poster without any editing
(save reducing the size) -- see the manual. Sciposter does work
for LaTeX, not just pdfLaTeX. However, xdvi produces strange
results, though a recent version of dvips does create good ps-
files from the dvi files. Also note that logos must either be
put in the current working directory or in the directories of
your LaTeX distribution. For some reason graphicspath settings
are ignored.

%package -n texlive-sciposter-doc
Summary:        Documentation for sciposter
Version:        svn15878.1.18

Provides:       tex-sciposter-doc
AutoReqProv:    No

%description -n texlive-sciposter-doc
Documentation for sciposter

%package -n texlive-sclang-prettifier
Provides:       tex-sclang-prettifier = %{tl_version}
License:        LPPL 1.3
Summary:        Prettyprinting SuperCollider source code
Version:        svn35087.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(textcomp.sty), tex(xcolor.sty), tex(listings.sty)
Provides:       tex(sclang-prettifier.sty) = %{tl_version}

%description -n texlive-sclang-prettifier
Built on top of the listings package, the package allows
effortless prettyprinting of SuperCollider source code in
documents typeset with LaTeX & friends.

%package -n texlive-sclang-prettifier-doc
Summary:        Documentation for sclang-prettifier
Version:        svn35087.0.1

Provides:       tex-sclang-prettifier-doc
AutoReqProv:    No

%description -n texlive-sclang-prettifier-doc
Documentation for sclang-prettifier

%package -n texlive-sfg
Provides:       tex-sfg = %{tl_version}
License:        LPPL
Summary:        Draw signal flow graphs
Version:        svn20209.0.91

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fp.sty), tex(pstricks.sty)
Provides:       tex(sfg.sty) = %{tl_version}

%description -n texlive-sfg
Defines some commands to draw signal flow graphs as used by
electrical and electronics engineers and graph theorists.
Requires fp and pstricks packages (and a relatively fast
machine).

%package -n texlive-sfg-doc
Summary:        Documentation for sfg
Version:        svn20209.0.91

Provides:       tex-sfg-doc
AutoReqProv:    No

%description -n texlive-sfg-doc
Documentation for sfg

%package -n texlive-screenplay
Provides:       tex-screenplay = %{tl_version}
License:        GPL+
Summary:        A class file to typeset screenplays
Version:        svn27223.1.6

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(geometry.sty), tex(courier.sty)
Provides:       tex(hardmarg.sty) = %{tl_version}, tex(screenplay.cls) = %{tl_version}

%description -n texlive-screenplay
The class implements the format recommended by the Academy of
Motion Picture Arts and Sciences.

%package -n texlive-screenplay-doc
Summary:        Documentation for screenplay
Version:        svn27223.1.6

Provides:       tex-screenplay-doc
AutoReqProv:    No

%description -n texlive-screenplay-doc
Documentation for screenplay

%package -n texlive-screenplay-pkg
Provides:       tex-screenplay-pkg = %{tl_version}
License:        LPPL 1.3
Summary:        Package version of the screenplay document class
Version:        svn44965
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifthen.sty), tex(setspace.sty)
Provides:       tex(screenplay-pkg.sty) = %{tl_version}

%description -n texlive-screenplay-pkg
This package implements the tools of the screenplay document
class in the form of a package so that screenplay fragments can
be included within another document class. For full
documentation of the available commands, please consult the
screenplay class documentation in addition to the included
package documentation.

%package -n texlive-screenplay-pkg-doc
Summary:        Documentation for screenplay-pkg
Version:        svn44965
Provides:       tex-screenplay-pkg-doc
AutoReqProv:    No

%description -n texlive-screenplay-pkg-doc
Documentation for screenplay-pkg
%package -n texlive-siunitx
Provides:       tex-siunitx = %{tl_version}
License:        LPPL 1.3
Summary:        A comprehensive (SI) units package
Version:        svn47746
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(expl3.sty), tex(xparse.sty), tex(amstext.sty), tex(array.sty)
Requires:       tex(l3keys2e.sty), tex(xspace.sty), tex(translator.sty)
Provides:       tex(siunitx-abbreviations.cfg) = %{tl_version}
Provides:       tex(siunitx-binary.cfg) = %{tl_version}, tex(siunitx-version-1.cfg) = %{tl_version}
Provides:       tex(siunitx.sty) = %{tl_version}

%package -n texlive-scrlttr2copy-doc
Provides:       tex-scrlttr2copy-doc = %{tl_version}
License:        LPPL
Summary:        doc files of scrlttr2copy
Version:        svn39734

AutoReqProv:    No

%description -n texlive-scrlttr2copy-doc
Documentation for scrlttr2copy

%package -n texlive-scrlttr2copy
Provides:       tex-scrlttr2copy = %{tl_version}
License:        LPPL
Summary:        A letter class option file for the automatic creation of copies
Version:        svn39734

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-scrlttr2copy
The file copy.lco provides the new class option "copy" for the
KOMA-Script letter class scrlttr2. If the option "copy" is
given, all pages of a specific letter are duplicated with
background text marking as copies.

%description -n texlive-siunitx
Typesetting values with units requires care to ensure that the
combined mathematical meaning of the value plus unit
combination is clear. In particular, the SI units system lays
down a consistent set of units with rules on how they are to be
used. However, different countries and publishers have
differing conventions on the exact appearance of numbers (and
units). A number of LaTeX packages have been developed to
provide consistent application of the various rules: SIunits,
sistyle, unitsdef and units are the leading examples. The
numprint package provides a large number of number-related
functions, while dcolumn and rccol provide tools for
typesetting tabular numbers. The siunitx package takes the best
from the existing packages, and adds new features and a
consistent interface. A number of new ideas have been
incorporated, to fill gaps in the existing provision. The
package also provides backward-compatibility with SIunits,
sistyle, unitsdef and units. The aim is to have one package to
handle all of the possible unit-related needs of LaTeX users.
The package relies on LaTeX 3 support from the l3kernel and
l3packages bundles.

%package -n texlive-siunitx-doc
Summary:        Documentation for siunitx
Version:        svn47746
Provides:       tex-siunitx-doc
AutoReqProv:    No

%description -n texlive-siunitx-doc
Documentation for siunitx

%package -n texlive-scheme-basic
Summary:        basic scheme (plain and latex)
Version:        svn25923.0
Requires:       texlive-base, texlive-collection-basic, texlive-collection-latex

%description -n texlive-scheme-basic
This is the basic TeX Live scheme: it is a small set of files
sufficient to typeset plain TeX or LaTeX documents in
PostScript or PDF, using the Computer Modern fonts.  This
scheme corresponds to collection-basic and collection-latex.

%package -n texlive-scheme-context
Summary:        ConTeXt scheme
Version:        svn35799.0
Requires:       texlive-base, texlive-collection-context
Requires:       texlive-collection-metapost, tex-tex-gyre
Requires:       tex-tex-gyre-math, tex-antt, tex-iwona, tex-kurier
Requires:       tex-poltawski, tex-xits, tex-asana-math, tex-gentium-tug
Requires:       tex-pxfonts, tex-txfonts, tex-ccicons, tex-eulervm
Requires:       tex-manfnt-font, tex-marvosym, tex-mflogo-font, tex-wasy
Requires:       tex-ly1
Provides:       tex(context) = %{tl_version}
Obsoletes:      texlive-texmf-context < %{tl_version}

%description -n texlive-scheme-context
This is the TeX Live scheme for installing ConTeXt.

%package -n texlive-scheme-full
Summary:        full scheme (everything)
Version:        svn44177
Requires:       texlive-base, texlive-collection-basic, texlive-collection-bibtexextra, texlive-collection-binextra
Requires:       texlive-collection-context, texlive-collection-fontsextra
Requires:       texlive-collection-fontsrecommended, texlive-collection-formatsextra
Requires:       texlive-collection-fontutils, texlive-collection-games
Requires:       texlive-collection-humanities, texlive-collection-langarabic
Requires:       texlive-collection-langchinese, texlive-collection-langcjk
Requires:       texlive-collection-langcyrillic, texlive-collection-langczechslovak
Requires:       texlive-collection-langenglish, texlive-collection-langeuropean
Requires:       texlive-collection-langfrench, texlive-collection-langgerman
Requires:       texlive-collection-langgreek, texlive-collection-langitalian
Requires:       texlive-collection-langjapanese, texlive-collection-langkorean
Requires:       texlive-collection-langother, texlive-collection-langpolish
Requires:       texlive-collection-langportuguese, texlive-collection-langspanish
Requires:       texlive-collection-latex, texlive-collection-latexextra
Requires:       texlive-collection-latexrecommended, texlive-collection-luatex
Requires:       texlive-collection-mathscience, texlive-collection-metapost
Requires:       texlive-collection-music, texlive-collection-pictures
Requires:       texlive-collection-plaingeneric, texlive-collection-pstricks
Requires:       texlive-collection-publishers, texlive-collection-texworks
Requires:       texlive-collection-xetex

%description -n texlive-scheme-full
This is the full TeX Live scheme: it installs everything
available.

%package -n texlive-scheme-gust
Summary:        GUST TeX Live scheme
Version:        svn44177
Requires:       texlive-base, texlive-FAQ-en-doc, texlive-Type1fonts-doc, texlive-amslatex-primer-doc
Requires:       texlive-amstex, texlive-antt, texlive-bibtex8, texlive-comment
Requires:       texlive-comprehensive-doc, texlive-concrete
Requires:       texlive-cyklop, texlive-dvidvi, texlive-dviljk, texlive-gustprog-doc
Requires:       texlive-impatient-doc, texlive-iwona, texlive-metafont-beginners-doc, texlive-metapost-examples-doc
Requires:       texlive-poltawski, texlive-seetexk, texlive-seminar, texlive-tds-doc
Requires:       texlive-tex4ht, texlive-texdoc, texlive-collection-basic, texlive-collection-context
Requires:       texlive-collection-fontutils, texlive-collection-fontsrecommended
Requires:       texlive-collection-langpolish, texlive-collection-latex
Requires:       texlive-collection-latexrecommended, texlive-collection-metapost
Requires:       texlive-collection-plaingeneric, texlive-collection-texworks
Requires:       texlive-collection-xetex

%description -n texlive-scheme-gust
This is the GUST TeX Live scheme: it is a set of files
sufficient to typeset Polish plain TeX, LaTeX and ConTeXt
documents in PostScript or PDF.

%package -n texlive-scheme-medium
Summary:        medium scheme (small + more packages and languages)
Version:        svn44177
Requires:       texlive-base, texlive-collection-basic, texlive-collection-binextra, texlive-collection-context
Requires:       texlive-collection-fontsrecommended, texlive-collection-fontutils
Requires:       texlive-collection-langczechslovak, texlive-collection-langenglish
Requires:       texlive-collection-langeuropean, texlive-collection-langfrench
Requires:       texlive-collection-langgerman, texlive-collection-langitalian
Requires:       texlive-collection-langpolish, texlive-collection-langportuguese
Requires:       texlive-collection-langspanish, texlive-collection-latex
Requires:       texlive-collection-latexrecommended, texlive-collection-luatex
Requires:       texlive-collection-mathscience, texlive-collection-metapost
Requires:       texlive-collection-plaingeneric, texlive-collection-texworks
Requires:       texlive-collection-xetex

%description -n texlive-scheme-medium
This is the medium TeX Live collection: it contains plain TeX,
LaTeX, many recommended packages, and support for most European
languages.

%package -n texlive-scheme-minimal
Summary:        minimal scheme (plain only)
Version:        svn13822.0
Requires:       texlive-base, texlive-collection-basic

%description -n texlive-scheme-minimal
This is the minimal TeX Live scheme, with support for only
plain TeX. (No LaTeX macros.)  LuaTeX is included because Lua
scripts are used in TeX Live infrastructure.  This scheme
corresponds exactly to collection-basic.

%package -n texlive-scheme-small
Summary:        small scheme (basic + xetex, metapost, a few languages)
Version:        svn41825
Requires:       texlive-base, texlive-collection-basic, texlive-collection-latex, texlive-collection-latexrecommended
Requires:       texlive-collection-metapost, texlive-collection-xetex
Requires:       texlive-ec, texlive-eurosym, texlive-lm, texlive-lualibs
Requires:       texlive-luaotfload, texlive-luatexbase, texlive-revtex, texlive-synctex
Requires:       texlive-times, texlive-tipa, texlive-ulem, texlive-upquote
Requires:       texlive-zapfding, texlive-babel-basque, texlive-hyphen-basque, texlive-babel-czech
Requires:       texlive-hyphen-czech, texlive-babel-danish
Requires:       texlive-hyphen-danish, texlive-babel-dutch
Requires:       texlive-hyphen-dutch, texlive-babel-english
Requires:       texlive-hyphen-english, texlive-babel-finnish
Requires:       texlive-hyphen-finnish, texlive-babel-french
Requires:       texlive-hyphen-french, texlive-babel-german
Requires:       texlive-hyphen-german, texlive-babel-hungarian
Requires:       texlive-hyphen-hungarian, texlive-babel-italian
Requires:       texlive-hyphen-italian, texlive-babel-norsk
Requires:       texlive-hyphen-norwegian, texlive-babel-polish
Requires:       texlive-hyphen-polish, texlive-babel-portuges
Requires:       texlive-hyphen-portuguese, texlive-babel-spanish
Requires:       texlive-hyphen-spanish, texlive-babel-swedish
Requires:       texlive-hyphen-swedish

%description -n texlive-scheme-small
This is a small TeX Live scheme, corresponding to MacTeX's
BasicTeX variant.  It adds XeTeX, MetaPost, various
hyphenations, and some recommended packages to scheme-basic.

%package -n texlive-scheme-tetex
Summary:        teTeX scheme (more than medium, but nowhere near full)
Version:        svn44187
Requires:       texlive-base, texlive-FAQ-en-doc, texlive-SIunits, texlive-acronym
Requires:       texlive-amslatex-primer-doc, texlive-bbm
Requires:       texlive-bbm-macros, texlive-bbold, texlive-bibtex8, texlive-ctie
Requires:       texlive-detex, texlive-dtl, texlive-dvi2tty, texlive-dvicopy
Requires:       texlive-dvidvi, texlive-dviljk, texlive-patgen, texlive-pdftools
Requires:       texlive-seetexk, texlive-tie, texlive-web, texlive-cmbright
Requires:       texlive-cweb, texlive-eplain, texlive-eulervm, texlive-gentle-doc
Requires:       texlive-lshort-english-doc, texlive-mltex
Requires:       texlive-multirow, texlive-nomencl, texlive-pst-pdf, texlive-rsfs
Requires:       texlive-subfigure, texlive-supertabular, texlive-tamethebeast-doc, texlive-tds-doc
Requires:       texlive-tex-refs-doc, texlive-collection-basic
Requires:       texlive-collection-context, texlive-collection-fontsrecommended
Requires:       texlive-collection-fontutils, texlive-collection-langcjk
Requires:       texlive-collection-langcyrillic, texlive-collection-langczechslovak
Requires:       texlive-collection-langenglish, texlive-collection-langeuropean
Requires:       texlive-collection-langfrench, texlive-collection-langgerman
Requires:       texlive-collection-langgreek, texlive-collection-langitalian
Requires:       texlive-collection-langother, texlive-collection-langpolish
Requires:       texlive-collection-langportuguese, texlive-collection-langspanish
Requires:       texlive-collection-latex, texlive-collection-latexrecommended
Requires:       texlive-collection-mathscience, texlive-collection-metapost
Requires:       texlive-collection-formatsextra, texlive-collection-pictures
Requires:       texlive-collection-plaingeneric, texlive-collection-pstricks
Provides:       tetex = 3.1-99
Obsoletes:      tetex < 3.1-99, texlive-dviutils < %{tl_version}

%description -n texlive-scheme-tetex
TeX Live scheme nearly equivalent to the teTeX distribution
that was maintained by Thomas Esser.

%package -n texlive-rosario-doc
Provides:       tex-rosario-doc = %{tl_version}
License:        LPPL and OFL
Summary:        doc files of rosario
Version:        svn40843

AutoReqProv:    No

%description -n texlive-rosario-doc
Documentation for rosario

%package -n texlive-rosario
Provides:       tex-rosario = %{tl_version}
License:        LPPL and OFL
Summary:        Using the free Rosario fonts with LaTeX
Version:        svn40843

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(Rosario.sty) = %{tl_version}, tex(Rosario.map) = %{tl_version}
Provides:       tex(OT1Rosario-LF.fd) = %{tl_version}, tex(T1Rosario-LF.fd) = %{tl_version}
Provides:       tex(TS1Rosario-LF.fd) = %{tl_version}, tex(LY1Rosario-LF.fd) = %{tl_version}
Provides:       tex(Rosario-BoldItalic.pfb) = %{tl_version}
Provides:       tex(Rosario-RegularLCDFJ.pfb) = %{tl_version}
Provides:       tex(Rosario-Bold.pfb) = %{tl_version}, tex(Rosario-Regular.pfb) = %{tl_version}
Provides:       tex(Rosario-ItalicLCDFJ.pfb) = %{tl_version}
Provides:       tex(Rosario-BoldLCDFJ.pfb) = %{tl_version}
Provides:       tex(Rosario-Italic.pfb) = %{tl_version}, tex(Rosario-BoldItalicLCDFJ.pfb) = %{tl_version}
Provides:       tex(ros_y2egj5.enc) = %{tl_version}, tex(ros_k6z3ge.enc) = %{tl_version}
Provides:       tex(ros_amohrd.enc) = %{tl_version}, tex(ros_c353pt.enc) = %{tl_version}
Provides:       tex(Rosario-Bold.otf) = %{tl_version}, tex(Rosario-Regular.otf) = %{tl_version}
Provides:       tex(Rosario-BoldItalic.otf) = %{tl_version}
Provides:       tex(Rosario-Italic.otf) = %{tl_version}, tex(Rosario-Italic-lf-ly1.vf) = %{tl_version}
Provides:       tex(Rosario-BoldItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(Rosario-Regular-lf-ly1.vf) = %{tl_version}
Provides:       tex(Rosario-Regular-lf-ts1.vf) = %{tl_version}
Provides:       tex(Rosario-Regular-lf-ot1.vf) = %{tl_version}
Provides:       tex(Rosario-Bold-lf-ts1.vf) = %{tl_version}
Provides:       tex(Rosario-BoldItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(Rosario-Italic-lf-t1.vf) = %{tl_version}
Provides:       tex(Rosario-Italic-lf-ot1.vf) = %{tl_version}
Provides:       tex(Rosario-Regular-lf-t1.vf) = %{tl_version}
Provides:       tex(Rosario-Bold-lf-t1.vf) = %{tl_version}
Provides:       tex(Rosario-Italic-lf-ts1.vf) = %{tl_version}
Provides:       tex(Rosario-Bold-lf-ly1.vf) = %{tl_version}
Provides:       tex(Rosario-Bold-lf-ot1.vf) = %{tl_version}
Provides:       tex(Rosario-BoldItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(Rosario-BoldItalic-lf-ot1.vf) = %{tl_version}
Provides:       tex(Rosario-BoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Rosario-Regular-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Rosario-Regular-lf-t1.tfm) = %{tl_version}
Provides:       tex(Rosario-Regular-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(Rosario-Bold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Rosario-Italic-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(Rosario-Italic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Rosario-Regular-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(Rosario-Italic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Rosario-Regular-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(Rosario-Bold-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(Rosario-BoldItalic-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(Rosario-BoldItalic-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(Rosario-Regular-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Rosario-Italic-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(Rosario-Bold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Rosario-Bold-lf-t1.tfm) = %{tl_version}
Provides:       tex(Rosario-BoldItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Rosario-Italic-lf-t1.tfm) = %{tl_version}
Provides:       tex(Rosario-Italic-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(Rosario-Regular-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Rosario-Bold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Rosario-Bold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Rosario-BoldItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Rosario-Bold-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(Rosario-Bold-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(Rosario-Regular-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Rosario-Italic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Rosario-Regular-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Rosario-Bold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Rosario-BoldItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Rosario-BoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(Rosario-BoldItalic-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(Rosario-Italic-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(Rosario-BoldItalic-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(Rosario-Regular-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(Rosario-Regular-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Rosario-Italic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Rosario-BoldItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Rosario-Bold-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(Rosario-Italic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Rosario-BoldItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Rosario-Italic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Rosario-Bold-lf-ot1.tfm) = %{tl_version}

%description -n texlive-rosario
The package provides the files required to use the Rosario
fonts with LaTeX. Rosario is a set of four fonts provided by
Hector Gatti, Adobe Typekit & Omnibus-Type Team under the Open
Font License (OFL), version 1.1. The fonts are copyright (c)
2012-2015, Omnibus-Type.

%package -n texlive-russ-doc
Provides:       tex-russ-doc = %{tl_version}
License:        LPPL
Summary:        doc files of russ
Version:        svn25209

AutoReqProv:    No

%description -n texlive-russ-doc
Documentation for russ

%package -n texlive-russ
Provides:       tex-russ = %{tl_version}
License:        LPPL
Summary:        LaTeX in Russian, without babel
Version:        svn25209

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(russ.sty) = %{tl_version}

%description -n texlive-russ
The package aims to facilitate Russian typesetting (based on
input using MicroSoft Code Page 1251). Russian hyphenation is
selected, and various mathematical commands are set up in
Russian style. Furthermore all Cyrillic letters' catcodes are
set to "letter", so that commands with Cyrillic letters in
their names may be defined.

%package -n texlive-sanitize-umlaut-doc
Provides:       tex-sanitize-umlaut-doc = %{tl_version}
License:        LPPL
Summary:        doc files of sanitize-umlaut
Version:        svn41365

AutoReqProv:    No

%description -n texlive-sanitize-umlaut-doc
Documentation for sanitize-umlaut

%package -n texlive-sanitize-umlaut
Provides:       tex-sanitize-umlaut = %{tl_version}
License:        LPPL
Summary:        sanitize umlauts for MakeIndex and pdfLaTeX
Version:        svn41365

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(sanitize-umlaut.sty) = %{tl_version}

%description -n texlive-sanitize-umlaut
This packages sanitizes umlauts to be used directly in index
entries for MakeIndex and friends with pdfLaTeX. This means
that inside \index an umlaut can be used as "U or as U. In both
cases, the letter is written as "U into the raw index file for
correct processing with MakeIndex and pdfLaTeX.

%package -n texlive-seuthesix-doc
Provides:       tex-seuthesix-doc = %{tl_version}
License:        GPLv3
Summary:        doc files of seuthesix
Version:        svn40088

AutoReqProv:    No

%description -n texlive-seuthesix-doc
Documentation for seuthesix

%package -n texlive-seuthesix
Provides:       tex-seuthesix = %{tl_version}
License:        GPLv3
Summary:        LaTeX class for theses at Southeast University, Nanjing, China
Version:        svn40088

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(seuthesix.cls) = %{tl_version}, tex(seuthesix.cfg) = %{tl_version}

%description -n texlive-seuthesix
This project provides a LaTeX document class as well as a
bibliography style file for typesetting theses at the Southeast
University, Nanjing, China. It is based on the seuthesis
package which, according to the author of seuthesix, is buggy
and has not been maintained for some time.

%package -n texlive-scientific-thesis-cover
Summary:        Provides cover page and affirmation at the end of a thesis
Version:        svn47923
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(scientific-thesis-cover.sty) = %{tl_version}

%description -n texlive-scientific-thesis-cover
Institutions require a cover page and an affirmation at the end
of a thesis. This package provides both.

%package -n texlive-rutitlepage
Summary:        Radboud University Titlepage Package
Version:        svn44485
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(rutitlepage.sty) = %{tl_version}

%description -n texlive-rutitlepage
This is an unofficial LaTeX package to generate titlepages for
the Radboud University, Nijmegen. It uses official vector logos
from the university. This package requires the following other
LaTeX packages: geometry, graphicx, ifpdf, keyval, iflang, and,
optionnaly, babel-dutch.

%package -n texlive-scratch
Summary:        Draw programs like "scratch"
Version:        svn47360
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(scratch.sty) = %{tl_version}

%description -n texlive-scratch
This package permits to draw program charts in the style of the
scatch project (scratch.mit.edu). It depends on the other LaTeX
packages TikZ and simplekv.

%package -n texlive-scsnowman
Summary:        Snowman variants using TikZ
Version:        svn47953
License:        BSD
Requires:       texlive-base texlive-kpathsea
Provides:       tex(scsnowman-normal.def) = %{tl_version}
Provides:       tex(scsnowman.sty) = %{tl_version}, tex(sctkzsym-base.sty) = %{tl_version}

%description -n texlive-scsnowman
This LaTeX package provides a command \scsnowman which can
display many variants of "snowman" ("yukidaruma" in Japanese).
TikZ is required for drawing these snowmen.

%package -n texlive-sesstime
Summary:        Session and timing information in lecture notes
Version:        svn46362
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(sesstime.sty) = %{tl_version}

%description -n texlive-sesstime
This LaTeX2e package makes it possible to add timing marks to
lecture notes in order to help managing the time available for
presenting a given section of the document. It also provides
tools to record and estimate the progress throughout the
course.

%package -n texlive-scratchx
Summary:        Include Scratch programs in LaTeX documents
Version:        svn44906
License:        LPPL
Requires:       texlive-base texlive-kpathsea, tex(calc.sty)
Requires:       tex(fp.sty), tex(ifsym.sty), tex(multido.sty), tex(tikz.sty)
Requires:       tex(xargs.sty), tex(xstring.sty)
Provides:       tex(ScratchX.sty) = %{tl_version}

%description -n texlive-scratchx
This package can be used to include every kind of Scratch
program in LaTeX documents. This may be particularly useful for
Math Teachers and IT specialists. The package depends on the
following other LaTeX packages: calc, fp, ifsym, multido, tikz,
xargs, and xstring.

%package -n texlive-sectionbreak
Summary:        LaTeX support for section breaks
Version:        svn46215
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(sectionbreak.sty) = %{tl_version}

%description -n texlive-sectionbreak
This package provides LaTeX support for section breaks, used
mainly in fiction books to signal changes in a story, like
changes in time, location, etc. It supports the asterism
symbol, text content, or custom macros as the section break
mark symbol.

%package -n texlive-semantic-markup
Summary:        Meaningful semantic markup in the spirit of the Text Encoding Initiative
Version:        svn47837
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(semantic-markup.sty) = %{tl_version}

%description -n texlive-semantic-markup
The package provides simple commands to allow authors
(especially scholars in the humanities) to write with a focus
on content rather than presentation. The commands are inspired
by the XML elements of the Text Encoding Initiative. Commands
like \term and \foreign are aliases for \emph. \quoted and
\soCalled are aliases for quoting commands. These commands
could be easily redefined for different formats. The package
also provides a footnote environment so that long footnotes can
be more cleanly separated from the main text. Because the
author is a music scholar, the package also includes some
macros for musical symbols and other basic notations for
musical analysis.

%package -n texlive-sexam
Summary:        Package for typesetting arabic exam scripts
Version:        svn46628
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(bacex.sty) = %{tl_version}, tex(sexam.sty) = %{tl_version}
Provides:       tex(wexam.sty) = %{tl_version}

%description -n texlive-sexam
The package provides a modified version of the exam package
made compatible with XeLaTeX/polyglossia to typesetting arabic.

%prep
%setup -q -c -T -a 3

%build

%install
install -d %{buildroot}%{_texdir}/../texmf
install -d %{buildroot}%{_texdir}/texmf-config/web2c
install -d %{buildroot}%{_var}/lib/texmf
install -d %{buildroot}%{_texdir}/texmf-dist
install -d %{buildroot}%{_texdir}/texmf-local

set +x
for i in %{sources}; do
  if [ "$i" != "%{_sourcedir}/texlive-licenses.tar.xz" ]; then
    if [ "$i" = "%{_sourcedir}/texlive-msg-translations.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/texworks.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/uplatex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.doc.tar.xz" ]; then
      OUTDIR="%{buildroot}%{_texdir}"
    else
      OUTDIR="%{buildroot}%{_texdir}/texmf-dist"
    fi
    xz -dc $i | tar x -C $OUTDIR
  fi
done
set -x

cur_dir=$PWD


install -d %{buildroot}%{_datadir}/fonts
cd %{buildroot}%{_datadir}/fonts
font_names="public/semaphor"
for i in ${font_names}; do
  j=`echo $i | cut -d / -f 2`
  ln -s %{_texdir}/texmf-dist/fonts/opentype/$i $j
done
cd $cur_dir


install -d %{buildroot}/%{_infodir}/
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/tlpkg/tlpobj/*

%files -n texlive-rsc
%license gpl.txt
%{_texdir}/texmf-dist/bibtex/bst/rsc/
%{_texdir}/texmf-dist/tex/latex/rsc/

%files -n texlive-rsc-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/rsc/

%files -n texlive-roboto
%license apache2.txt
%{_texdir}/texmf-dist/fonts/afm/google/roboto/
%{_texdir}/texmf-dist/fonts/enc/dvips/roboto/
%{_texdir}/texmf-dist/fonts/map/dvips/roboto/
%{_texdir}/texmf-dist/fonts/pfm/google/roboto/
%{_texdir}/texmf-dist/fonts/tfm/google/roboto/
%{_texdir}/texmf-dist/fonts/truetype/google/roboto/
%{_texdir}/texmf-dist/fonts/type1/google/roboto/
%{_texdir}/texmf-dist/fonts/vf/google/roboto/
%{_texdir}/texmf-dist/tex/latex/roboto/

%files -n texlive-roboto-doc
%license apache2.txt
%{_texdir}/texmf-dist/doc/fonts/roboto/

%files -n texlive-romande
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/afm/arkandis/romande/
%{_texdir}/texmf-dist/fonts/enc/dvips/romande/
%{_texdir}/texmf-dist/fonts/map/dvips/romande/
%{_texdir}/texmf-dist/fonts/tfm/arkandis/romande/
%{_texdir}/texmf-dist/fonts/type1/arkandis/romande/
%{_texdir}/texmf-dist/fonts/vf/arkandis/romande/
%{_texdir}/texmf-dist/tex/latex/romande/

%files -n texlive-romande-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/romande/

%files -n texlive-rosario-doc
%license lppl1.3.txt ofl.txt
%{_texdir}/texmf-dist/doc/fonts/rosario/

%files -n texlive-rosario
%license lppl1.3.txt ofl.txt
%{_texdir}/texmf-dist/tex/latex/rosario/
%{_texdir}/texmf-dist/fonts/opentype/public/rosario/
%{_texdir}/texmf-dist/fonts/map/dvips/rosario/
%{_texdir}/texmf-dist/fonts/tfm/public/rosario/
%{_texdir}/texmf-dist/fonts/vf/public/rosario/
%{_texdir}/texmf-dist/fonts/enc/dvips/rosario/
%{_texdir}/texmf-dist/fonts/type1/public/rosario/

%files -n texlive-rsfso
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/map/dvips/rsfso/
%{_texdir}/texmf-dist/fonts/tfm/public/rsfso/
%{_texdir}/texmf-dist/fonts/vf/public/rsfso/
%{_texdir}/texmf-dist/tex/latex/rsfso/

%files -n texlive-rsfso-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/rsfso/

%files -n texlive-rsfs
%{_texdir}/texmf-dist/fonts/afm/public/rsfs/
%{_texdir}/texmf-dist/fonts/map/dvips/rsfs/
%{_texdir}/texmf-dist/fonts/source/public/rsfs/
%{_texdir}/texmf-dist/fonts/tfm/public/rsfs/
%{_texdir}/texmf-dist/fonts/type1/public/rsfs/
%{_texdir}/texmf-dist/tex/plain/rsfs/

%files -n texlive-rsfs-doc
%{_texdir}/texmf-dist/doc/fonts/rsfs/

%files -n texlive-robustcommand
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/robustcommand/

%files -n texlive-robustcommand-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/robustcommand/

%files -n texlive-robustindex
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/robustindex/

%files -n texlive-robustindex-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/robustindex/

%files -n texlive-romanbar
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/romanbar/

%files -n texlive-romanbar-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/romanbar/

%files -n texlive-r_und_s
%{_texdir}/texmf-dist/tex/latex/r_und_s/

%files -n texlive-r_und_s-doc
%{_texdir}/texmf-dist/doc/latex/r_und_s/

%files -n texlive-romanbarpagenumber
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/romanbarpagenumber/

%files -n texlive-romanbarpagenumber-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/romanbarpagenumber/

%files -n texlive-romanneg
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/romanneg/

%files -n texlive-romanneg-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/romanneg/

%files -n texlive-romannum
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/romannum/

%files -n texlive-romannum-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/romannum/

%files -n texlive-rotfloat
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/rotfloat/

%files -n texlive-rotfloat-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/rotfloat/

%files -n texlive-rotpages
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/rotpages/

%files -n texlive-rotpages-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/rotpages/

%files -n texlive-roundbox
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/roundbox/

%files -n texlive-roundbox-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/roundbox/

%files -n texlive-rterface
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/rterface/

%files -n texlive-rterface-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/rterface/

%files -n texlive-rtkinenc
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/rtkinenc/

%files -n texlive-rtkinenc-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/rtkinenc/

%files -n texlive-rrgtrees
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/rrgtrees/

%files -n texlive-rrgtrees-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/rrgtrees/

%files -n texlive-rtklage
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/rtklage/

%files -n texlive-rtklage-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/rtklage/

%files -n texlive-rulercompass
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/rulercompass/

%files -n texlive-rulercompass-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/rulercompass/

%files -n texlive-rvwrite
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/rvwrite/

%files -n texlive-rvwrite-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/rvwrite/

%files -n texlive-sansmathaccent
%license lppl1.3.txt
%{_texdir}/texmf-dist/fonts/map/dvips/sansmathaccent/
%{_texdir}/texmf-dist/fonts/tfm/public/sansmathaccent/
%{_texdir}/texmf-dist/fonts/vf/public/sansmathaccent/
%{_texdir}/texmf-dist/tex/latex/sansmathaccent/

%files -n texlive-sansmathaccent-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/fonts/sansmathaccent/

%files -n texlive-sansmathfonts
%license lppl1.3.txt
%{_texdir}/texmf-dist/fonts/map/dvips/sansmathfonts/
%{_texdir}/texmf-dist/fonts/source/public/sansmathfonts/
%{_texdir}/texmf-dist/fonts/tfm/public/sansmathfonts/
%{_texdir}/texmf-dist/fonts/type1/public/sansmathfonts/
%{_texdir}/texmf-dist/fonts/vf/public/sansmathfonts/
%{_texdir}/texmf-dist/tex/latex/sansmathfonts/

%files -n texlive-sansmathfonts-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/fonts/sansmathfonts/

%files -n texlive-sauter
%license gpl.txt
%{_texdir}/texmf-dist/fonts/source/public/sauter/

%files -n texlive-sauterfonts
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/sauterfonts/

%files -n texlive-sauterfonts-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/sauterfonts/

%files -n texlive-savetrees
%license lppl1.3.txt
%{_texdir}/texmf-dist/bibtex/bst/savetrees/
%{_texdir}/texmf-dist/tex/latex/savetrees/

%files -n texlive-savetrees-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/savetrees/

%files -n texlive-seuthesis
%license gpl3.txt
%{_texdir}/texmf-dist/bibtex/bst/seuthesis/

%files -n texlive-seuthesis-doc
%license gpl3.txt
%{_texdir}/texmf-dist/doc/latex/seuthesis/

%files -n texlive-sanskrit
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/source/public/sanskrit/
%{_texdir}/texmf-dist/fonts/tfm/public/sanskrit/
%{_texdir}/texmf-dist/tex/latex/sanskrit/

%files -n texlive-sanskrit-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/sanskrit/

%files -n texlive-russ-doc
%license lppl.txt
%{_texdir}/texmf-dist/doc/latex/russ/

%files -n texlive-russ
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/russ/

%files -n texlive-schulschriften
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/source/public/schulschriften/
%{_texdir}/texmf-dist/fonts/tfm/public/schulschriften/
%{_texdir}/texmf-dist/tex/latex/schulschriften/

%files -n texlive-schulschriften-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/schulschriften/

%files -n texlive-semaphor
%license gpl.txt
%{_datadir}/fonts/semaphor
%{_texdir}/texmf-dist/fonts/afm/public/semaphor/
%{_texdir}/texmf-dist/fonts/enc/dvips/semaphor/
%{_texdir}/texmf-dist/fonts/map/dvips/semaphor/
%{_texdir}/texmf-dist/fonts/opentype/public/semaphor/
%{_texdir}/texmf-dist/fonts/source/public/semaphor/
%{_texdir}/texmf-dist/fonts/tfm/public/semaphor/
%{_texdir}/texmf-dist/fonts/type1/public/semaphor/
%{_texdir}/texmf-dist/tex/context/third/semaphor/
%{_texdir}/texmf-dist/tex/latex/semaphor/
%{_texdir}/texmf-dist/tex/plain/semaphor/

%files -n texlive-semaphor-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/fonts/semaphor/

%files -n texlive-schwalbe-chess
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/schwalbe-chess/

%files -n texlive-schwalbe-chess-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/schwalbe-chess/

%files -n texlive-sgame
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/sgame/

%files -n texlive-sgame-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/sgame/

%files -n texlive-schemata
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/schemata/

%files -n texlive-schemata-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/schemata/

%files -n texlive-rviewport
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/rviewport/

%files -n texlive-rviewport-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/rviewport/

%files -n texlive-sa-tikz
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/sa-tikz/

%files -n texlive-sa-tikz-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/sa-tikz/

%files -n texlive-schemabloc
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/schemabloc/

%files -n texlive-schemabloc-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/schemabloc/

%files -n texlive-setdeck
%license gpl3.txt
%{_texdir}/texmf-dist/tex/latex/setdeck/

%files -n texlive-setdeck-doc
%license gpl3.txt
%{_texdir}/texmf-dist/doc/latex/setdeck/

%files -n texlive-rutitlepage
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/rutitlepage/
%{_texdir}/texmf-dist/tex/latex/rutitlepage/

%files -n texlive-scratch
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/scratch/
%{_texdir}/texmf-dist/tex/latex/scratch/

%files -n texlive-scsnowman
%license bsd.txt
%doc %{_texdir}/texmf-dist/doc/latex/scsnowman/
%{_texdir}/texmf-dist/tex/latex/scsnowman/

%files -n texlive-sesstime
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/sesstime/
%{_texdir}/texmf-dist/tex/latex/sesstime/

%files -n texlive-scientific-thesis-cover
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/scientific-thesis-cover/
%doc %{_texdir}/texmf-dist/doc/latex/scientific-thesis-cover/

%files -n texlive-scratchx
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/scratchx/
%doc %{_texdir}/texmf-dist/doc/latex/scratchx/

%files -n texlive-sectionbreak
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/sectionbreak/
%doc %{_texdir}/texmf-dist/doc/latex/sectionbreak/

%files -n texlive-semantic-markup
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/semantic-markup/
%doc %{_texdir}/texmf-dist/doc/latex/semantic-markup/

%files -n texlive-sexam
%license lppl.txt
%{_texdir}/texmf-dist/tex/xelatex/sexam/
%doc %{_texdir}/texmf-dist/doc/xelatex/sexam/

%files -n texlive-ryethesis
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/ryethesis/

%files -n texlive-ryethesis-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/ryethesis/

%files -n texlive-sageep
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/sageep/
%{_texdir}/texmf-dist/tex/latex/sageep/

%files -n texlive-sageep-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/sageep/

%files -n texlive-sapthesis
%license lppl1.3.txt
%{_texdir}/texmf-dist/bibtex/bst/sapthesis/
%{_texdir}/texmf-dist/tex/latex/sapthesis/

%files -n texlive-sapthesis-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/sapthesis/

%files -n texlive-scrjrnl
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/scrjrnl/

%files -n texlive-scrjrnl-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/scrjrnl/

%files -n texlive-schule
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/schule/

%files -n texlive-schule-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/schule/

%files -n texlive-seuthesix-doc
%license gpl3.txt
%{_texdir}/texmf-dist/doc/latex/seuthesix/

%files -n texlive-seuthesix
%license gpl3.txt
%{_texdir}/texmf-dist/tex/latex/seuthesix/
%{_texdir}/texmf-dist/bibtex/bst/seuthesix/

%files -n texlive-sanskrit-t1
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/map/dvips/sanskrit-t1/
%{_texdir}/texmf-dist/fonts/type1/public/sanskrit-t1/

%files -n texlive-sanskrit-t1-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/sanskrit-t1/

%files -n texlive-sanitize-umlaut-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/sanitize-umlaut/

%files -n texlive-sanitize-umlaut
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/sanitize-umlaut/

%files -n texlive-sansmath
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/sansmath/

%files -n texlive-sansmath-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/sansmath/

%files -n texlive-sasnrdisplay
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/sasnrdisplay/

%files -n texlive-sasnrdisplay-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/sasnrdisplay/

%files -n texlive-sauerj
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/sauerj/

%files -n texlive-sauerj-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/sauerj/

%files -n texlive-savefnmark
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/savefnmark/

%files -n texlive-savefnmark-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/savefnmark/

%files -n texlive-scale
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/scale/

%files -n texlive-scale-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/scale/

%files -n texlive-scalebar
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/scalebar/

%files -n texlive-scalebar-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/scalebar/

%files -n texlive-scalerel
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/scalerel/

%files -n texlive-scalerel-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/scalerel/

%files -n texlive-scanpages
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/scanpages/
%{_texdir}/texmf-dist/fonts/map/dvips/scanpages/
%{_texdir}/texmf-dist/fonts/tfm/public/scanpages/
%{_texdir}/texmf-dist/fonts/type1/public/scanpages/

%files -n texlive-scanpages-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/scanpages/

%files -n texlive-sciposter
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/sciposter/

%files -n texlive-sciposter-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/sciposter/

%files -n texlive-sclang-prettifier
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/sclang-prettifier/

%files -n texlive-sclang-prettifier-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/sclang-prettifier/

%files -n texlive-sfg
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/sfg/

%files -n texlive-sfg-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/sfg/

%files -n texlive-screenplay
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/screenplay/

%files -n texlive-screenplay-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/screenplay/

%files -n texlive-screenplay-pkg
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/screenplay-pkg/

%files -n texlive-screenplay-pkg-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/screenplay-pkg/

%files -n texlive-scrlttr2copy-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/scrlttr2copy/

%files -n texlive-scrlttr2copy
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/scrlttr2copy/

%files -n texlive-sdrt
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/sdrt/

%files -n texlive-sdrt-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/sdrt/

%files -n texlive-sduthesis
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/sduthesis/

%files -n texlive-sduthesis-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/sduthesis/

%files -n texlive-secdot
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/secdot/

%files -n texlive-secdot-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/secdot/

%files -n texlive-sectionbox
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/sectionbox/

%files -n texlive-sectionbox-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/sectionbox/

%files -n texlive-seminar
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/seminar/

%files -n texlive-seminar-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/seminar/

%files -n texlive-ruhyphen
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/ruhyphen/

%files -n texlive-section
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/section/

%files -n texlive-section-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/section/

%files -n texlive-sectsty
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/sectsty/

%files -n texlive-sectsty-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/sectsty/

%files -n texlive-seealso
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/seealso/

%files -n texlive-seealso-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/seealso/

%files -n texlive-selectp
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/selectp/

%files -n texlive-selectp-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/selectp/

%files -n texlive-selnolig
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/lualatex/selnolig/

%files -n texlive-selnolig-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/lualatex/selnolig/

%files -n texlive-semantic
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/semantic/

%files -n texlive-semantic-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/semantic/

%files -n texlive-semioneside
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/semioneside/

%files -n texlive-semioneside-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/semioneside/

%files -n texlive-semproc
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/semproc/

%files -n texlive-semproc-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/semproc/

%files -n texlive-sepfootnotes
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/sepfootnotes/

%files -n texlive-sepfootnotes-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/sepfootnotes/

%files -n texlive-sepnum
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/sepnum/

%files -n texlive-sepnum-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/sepnum/

%files -n texlive-seqsplit
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/seqsplit/

%files -n texlive-seqsplit-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/seqsplit/

%files -n texlive-serbian-apostrophe
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/serbian-apostrophe/

%files -n texlive-serbian-apostrophe-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/serbian-apostrophe/

%files -n texlive-serbian-date-lat
%license gpl2.txt
%{_texdir}/texmf-dist/tex/latex/serbian-date-lat/

%files -n texlive-serbian-date-lat-doc
%license gpl2.txt
%{_texdir}/texmf-dist/doc/latex/serbian-date-lat/

%files -n texlive-serbian-def-cyr
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/serbian-def-cyr/

%files -n texlive-serbian-def-cyr-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/serbian-def-cyr/

%files -n texlive-serbian-lig
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/serbian-lig/

%files -n texlive-serbian-lig-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/serbian-lig/

%files -n texlive-sesamanuel
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/sesamanuel/

%files -n texlive-sesamanuel-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/sesamanuel/

%files -n texlive-setspace
%{_texdir}/texmf-dist/tex/latex/setspace/

%files -n texlive-setspace-doc
%{_texdir}/texmf-dist/doc/latex/setspace/

%files -n texlive-sf298
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/sf298/

%files -n texlive-sf298-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/sf298/

%files -n texlive-sffms
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/sffms/

%files -n texlive-sffms-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/sffms/

%files -n texlive-roundrect
%license lppl1.3.txt
%{_texdir}/texmf-dist/metapost/roundrect/

%files -n texlive-roundrect-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/metapost/roundrect/

%files -n texlive-roex
%{_texdir}/texmf-dist/metafont/roex/

%files -n texlive-savesym
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/savesym/

%files -n texlive-sfmath
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/sfmath/

%changelog
* Wed May 19 2021 maminjie <maminjie1@huawei.com> - 8:2018-24
- split texlive

* Fri Sep 11 2020 Guoshuai Sun <sunguoshuai@huawei.com> - 8:2018-23
- Drop texlive-texinfo,use new files in texinfo-tex instead

* Sun Jan 19 2020 daiqianwen <daiqianwen@huawei.com> - 8:2018-22
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: modify spec

* Tue Dec 10 2019 Jiangping Hu <hujiangping@huawei.com> - 8:2018-21
- Package init
