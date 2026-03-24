## FontSpector report

fontspector version: 1.4.0



## Checks with FATAL results

These must be addressed first.


<details><summary>[1] fonts/Obvia/variable/Obvia[wght].ttf</summary>
<div>


<details>
    <summary>💥 <b>ERROR</b> Familyname must be unique according to namecheck.fontdata.com (fontdata_namecheck)</summary>
    <div>








- 💥 **ERROR** Error: A network error occurred: Failed to access: http://namecheck.fontdata.com/. error sending request for url (http://namecheck.fontdata.com/api/?q=Obvia) 
  
  

</div>
</details>


</div>
</details>


<details><summary>[1] fonts/Obvia/variable/Obvia-Italic[wght].ttf</summary>
<div>


<details>
    <summary>💥 <b>ERROR</b> Familyname must be unique according to namecheck.fontdata.com (fontdata_namecheck)</summary>
    <div>








- 💥 **ERROR** Error: A network error occurred: Failed to access: http://namecheck.fontdata.com/. error sending request for url (http://namecheck.fontdata.com/api/?q=Obvia) 
  
  

</div>
</details>


</div>
</details>







## All other checks




<details><summary>[11] fonts/Obvia/variable/Obvia-Italic[wght].ttf</summary>
<div>


<details>
    <summary>⚠️ <b>WARN</b> Check accent of Lcaron, dcaron, lcaron, tcaron (alt_caron)</summary>
    <div>








- ⚠️ **WARN** tcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. (contour_count)</summary>
    <div>








- ⚠️ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are
     inferred from the typical amounts of contours observed in a
     large collection of reference font families. The divergences
     listed below may simply indicate a significantly different
     design on some of your glyphs. On the other hand, some of these
     may flag actual bugs in the font such as glyphs mapped to an
     incorrect codepoint. Please consider reviewing the design and
     codepoint assignment of these to make sure they are correct.


    The following glyphs do not have the recommended number of contours:
* uni0430.ss01 (unencoded): found 1, expected one of: {3, 2, 5}
* uni24FF (U+24FF): found 4, expected one of: {3}
* radical (U+221A): found 3, expected one of: {2, 1} [code: contour-count]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Are there caret positions declared for every ligature? (ligature_carets)</summary>
    <div>








- ⚠️ **WARN** This font lacks caret positioning values for these ligature glyphs:

* A_I.dlig
* U_I.dlig [code: incomplete-caret-pos-data]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure variable fonts include an avar table. (mandatory_avar_table)</summary>
    <div>








- ⚠️ **WARN** The font does not include an avar table. [code: missing-avar]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. (math_signs_width)</summary>
    <div>








- ⚠️ **WARN** The most common width is 545 among a set of 13  math glyphs.
The following math glyphs have a different width, though:
width=522: approxequal
width=540: equal, notequal
width=559: plus
width=507: multiply
width=546: greaterequal
width=500: logicalnot
width=541: divide
width=539: plusminus
width=520: minus [code: width-outliers]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs (unreachable_glyphs)</summary>
    <div>








- ⚠️ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

* blackCircled [code: unreachable-glyphs]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Glyph names are all valid? (valid_glyphnames)</summary>
    <div>








- ⚠️ **WARN** The following glyph names are too long: "hyphen_hyphen_hyphen_greater.liga, periodcentered.loclCAT.case.ss08" [code: legacy-long-names]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Shapes languages in all GF glyphsets. (googlefonts/glyphsets/shape_languages)</summary>
    <div>








- ⚠️ **WARN** Warning language shaping:

| Message                                                               | Languages              |
|-----------------------------------------------------------------------|------------------------|
| Auxiliary orthography codepoints:                                     | * en_Latn (English)    |
|   The following auxiliary characters are missing from the font: ʻ     |                        |
| Auxiliary orthography codepoints:                                     | * uk_Cyrl (Ukrainian)  |
|   Shaper didn't attach acutecomb to uni0430 when shaping the text 'а́' |                        |
|   Shaper didn't attach acutecomb to uni0435 when shaping the text 'е́' |                        |
|   Shaper didn't attach acutecomb to uni0454 when shaping the text 'є́' |                        |
|   Shaper didn't attach acutecomb to uni0438 when shaping the text 'и́' |                        |
|   Shaper didn't attach acutecomb to uni0456 when shaping the text 'і́' |                        |
|   Shaper didn't attach acutecomb to uni0457 when shaping the text 'ї́' |                        |
|   Shaper didn't attach acutecomb to uni043E when shaping the text 'о́' |                        |
|   Shaper didn't attach acutecomb to uni0443 when shaping the text 'у́' |                        |
|   Shaper didn't attach acutecomb to uni044E when shaping the text 'ю́' |                        |
|   Shaper didn't attach acutecomb to uni044F when shaping the text 'я́' |                        |
| Auxiliary orthography codepoints:                                     | * be_Cyrl (Belarusian) |
|   Shaper didn't attach acutecomb to uni0430 when shaping the text 'а́' |                        |
|   Shaper didn't attach acutecomb to uni0435 when shaping the text 'е́' |                        |
|   Shaper didn't attach acutecomb to uni0451 when shaping the text 'ё́' |                        |
|   Shaper didn't attach acutecomb to uni0456 when shaping the text 'і́' |                        |
|   Shaper didn't attach acutecomb to uni043E when shaping the text 'о́' |                        |
|   Shaper didn't attach acutecomb to uni0443 when shaping the text 'у́' |                        |
|   Shaper didn't attach acutecomb to uni044B when shaping the text 'ы́' |                        |
|   Shaper didn't attach acutecomb to uni044D when shaping the text 'э́' |                        |
|   Shaper didn't attach acutecomb to uni044E when shaping the text 'ю́' |                        |
|   Shaper didn't attach acutecomb to uni044F when shaping the text 'я́' |                        |
| Auxiliary orthography codepoints:                                     | * ca_Latn (Catalan)    |
|   The following auxiliary characters are missing from the font: Ŀ     |                        |
|   The following auxiliary characters are missing from the font: ŀ     |                        |
| Auxiliary orthography codepoints:                                     | * fi_Latn (Finnish)    |
|   The following auxiliary characters are missing from the font: Ʒ     |                        |
|   The following auxiliary characters are missing from the font: Ǯ     |                        |
|   The following auxiliary characters are missing from the font: ʒ     |                        |
|   The following auxiliary characters are missing from the font: ǯ     |                        |
| Auxiliary orthography codepoints:                                     | * ru_Cyrl (Russian)    |
|   Shaper didn't attach acutecomb to uni0430 when shaping the text 'а́' |                        |
|   Shaper didn't attach acutecomb to uni0435 when shaping the text 'е́' |                        |
|   Shaper didn't attach acutecomb to uni0438 when shaping the text 'и́' |                        |
|   Shaper didn't attach acutecomb to uni043E when shaping the text 'о́' |                        |
|   Shaper didn't attach acutecomb to uni0443 when shaping the text 'у́' |                        |
|   Shaper didn't attach acutecomb to uni044B when shaping the text 'ы́' |                        |
|   Shaper didn't attach acutecomb to uni044D when shaping the text 'э́' |                        |
|   Shaper didn't attach acutecomb to uni044E when shaping the text 'ю́' |                        |
|   Shaper didn't attach acutecomb to uni044F when shaping the text 'я́' |                        |
| Auxiliary orthography codepoints:                                     | * de_Latn (German)     |
|   The following auxiliary characters are missing from the font: ſ     | * fr_Latn (French)     |
| Auxiliary orthography codepoints:                                     | * bg_Cyrl (Bulgarian)  |
|   Shaper didn't attach gravecomb to uni0430 when shaping the text 'а̀' |                        |
|   Shaper didn't attach gravecomb to uni043E when shaping the text 'о̀' |                        |
|   Shaper didn't attach gravecomb to uni0443 when shaping the text 'у̀' |                        |
|   Shaper didn't attach gravecomb to uni044A when shaping the text 'ъ̀' |                        |
|   Shaper didn't attach gravecomb to uni044E when shaping the text 'ю̀' |                        |
|   Shaper didn't attach gravecomb to uni044F when shaping the text 'я̀' |                        |
| Auxiliary orthography codepoints:                                     | * sr_Cyrl (Serbian)    |
|   Shaper didn't attach uni0302 to uni0430 when shaping the text 'а̂'   |                        |
|   Shaper didn't attach uni0302 to uni0435 when shaping the text 'е̂'   |                        |
|   Shaper didn't attach uni0302 to uni0438 when shaping the text 'и̂'   |                        |
|   Shaper didn't attach uni0302 to uni043E when shaping the text 'о̂'   |                        |
|   Shaper didn't attach uni0302 to uni0443 when shaping the text 'у̂'   |                        | [code: warning-language-shaping]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Font has correct separator glyphs? (googlefonts/separator_glyphs)</summary>
    <div>








- ⚠️ **WARN** The following separator glyphs are missing:

* U+2028
* U+2029 [code: missing-separator-glyphs]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that
replace the dot. (soft_dotted)</summary>
    <div>








- ⚠️ **WARN** The dot of soft dotted characters used in orthographies _must_ disappear in the following strings:

* і́
* ị̀
* ị̃
* ị̂
* ị̄
* ị́
* į̀
* į̃
* į̂
* į̄
* į̌
* į́The dot of soft dotted characters _should_ disappear in other cases, for example:

* і̨̉
* і̨̀
* і̨̃
* і̨̂
* і̨̄
* і̨̇
* і̨̊
* і̨̌
* і̨̒
* і̨̆
* і̨̋
* і̨́
* і̷̉
* і̷̀
* і̷̃
* і̷̂
* і̷̄
* і̷̇
* і̷̊
* і̷̌
* і̷̒
* і̷̆
* і̷̋
* і̷́
* і̸̉
* і̸̀
* і̸̃
* і̸̂
* і̸̄
* і̸̇
* і̸̊
* і̸̌
* і̸̒
* і̸̆
* і̸̋
* і̸́
* і̦̉
* і̦̀
* і̦̃
* і̦̂
* і̦̄
* і̦̇
* і̦̊
* і̦̌
* і̦̒
* і̦̆
* і̦̋
* і̦́
* і̛̉
* і̛̀
* і̛̃
* і̛̂
* і̛̄
* і̛̇
* і̛̊
* і̛̌
* і̛̒
* і̛̆
* і̛̋
* і̛́
* і̣̉
* і̣̀
* і̣̃
* і̣̂
* і̣̄
* і̣̇
* і̣̊
* і̣̌
* і̣̒
* і̣̆
* і̣̋
* і̣́
* і̧̉
* і̧̀
* і̧̃
* і̧̂
* і̧̄
* і̧̇
* і̧̊
* і̧̌
* і̧̒
* і̧̆
* і̧̋
* і̧́
* і̵̉
* і̵̀
* і̵̃
* і̵̂
* і̵̄
* і̵̇
* і̵̊
* і̵̌
* і̵̒
* і̵̆
* і̵̋
* і̵́
* і̶̉
* і̶̀
* і̶̃
* і̶̂
* і̶̄
* і̶̇
* і̶̊
* і̶̌
* і̶̒
* і̶̆
* і̶̋
* і̶́
* і̉
* і̀
* і̃
* і̂
* і̄
* і̇
* і̊
* і̌
* і̒
* і̆
* і̋
* ị̷̉
* ị̷̀
* ị̷̃
* ị̷̂
* ị̷̄
* ị̷̇
* ị̷̊
* ị̷̌
* ị̷̒
* ị̷̆
* ị̷̋
* ị̷́
* ị̷̈
* ị̸̉
* ị̸̀
* ị̸̃
* ị̸̂
* ị̸̄
* ị̸̇
* ị̸̊
* ị̸̌
* ị̸̒
* ị̸̆
* ị̸̋
* ị̸́
* ị̸̈
* ị̦̉
* ị̦̀
* ị̦̃
* ị̦̂
* ị̦̄
* ị̦̇
* ị̦̊
* ị̦̌
* ị̦̒
* ị̦̆
* ị̦̋
* ị̦́
* ị̦̈
* ị̛̉
* ị̛̀
* ị̛̃
* ị̛̂
* ị̛̄
* ị̛̇
* ị̛̊
* ị̛̌
* ị̛̒
* ị̛̆
* ị̛̋
* ị̛́
* ị̛̈
* ị̣̉
* ị̣̀
* ị̣̃
* ị̣̂
* ị̣̄
* ị̣̇
* ị̣̊
* ị̣̌
* ị̣̒
* ị̣̆
* ị̣̋
* ị̣́
* ị̣̈
* ị̧̉
* ị̧̀
* ị̧̃
* ị̧̂
* ị̧̄
* ị̧̇
* ị̧̊
* ị̧̌
* ị̧̒
* ị̧̆
* ị̧̋
* ị̧́
* ị̧̈
* ị̵̉
* ị̵̀
* ị̵̃
* ị̵̂
* ị̵̄
* ị̵̇
* ị̵̊
* ị̵̌
* ị̵̒
* ị̵̆
* ị̵̋
* ị̵́
* ị̵̈
* ị̶̉
* ị̶̀
* ị̶̃
* ị̶̂
* ị̶̄
* ị̶̇
* ị̶̊
* ị̶̌
* ị̶̒
* ị̶̆
* ị̶̋
* ị̶́
* ị̶̈
* ị̉
* ị̇
* ị̊
* ị̌
* ị̒
* ị̆
* ị̋
* ị̈
* ј̨̉
* ј̨̀
* ј̨̃
* ј̨̂
* ј̨̄
* ј̨̇
* ј̨̊
* ј̨̌
* ј̨̒
* ј̨̆
* ј̨̋
* ј̨́
* ј̨̈
* ј̷̉
* ј̷̀
* ј̷̃
* ј̷̂
* ј̷̄
* ј̷̇
* ј̷̊
* ј̷̌
* ј̷̒
* ј̷̆
* ј̷̋
* ј̷́
* ј̷̈
* ј̸̉
* ј̸̀
* ј̸̃
* ј̸̂
* ј̸̄
* ј̸̇
* ј̸̊
* ј̸̌
* ј̸̒
* ј̸̆
* ј̸̋
* ј̸́
* ј̸̈
* ј̦̉
* ј̦̀
* ј̦̃
* ј̦̂
* ј̦̄
* ј̦̇
* ј̦̊
* ј̦̌
* ј̦̒
* ј̦̆
* ј̦̋
* ј̦́
* ј̦̈
* ј̛̉
* ј̛̀
* ј̛̃
* ј̛̂
* ј̛̄
* ј̛̇
* ј̛̊
* ј̛̌
* ј̛̒
* ј̛̆
* ј̛̋
* ј̛́
* ј̛̈
* ј̣̉
* ј̣̀
* ј̣̃
* ј̣̂
* ј̣̄
* ј̣̇
* ј̣̊
* ј̣̌
* ј̣̒
* ј̣̆
* ј̣̋
* ј̣́
* ј̣̈
* ј̧̉
* ј̧̀
* ј̧̃
* ј̧̂
* ј̧̄
* ј̧̇
* ј̧̊
* ј̧̌
* ј̧̒
* ј̧̆
* ј̧̋
* ј̧́
* ј̧̈
* ј̵̉
* ј̵̀
* ј̵̃
* ј̵̂
* ј̵̄
* ј̵̇
* ј̵̊
* ј̵̌
* ј̵̒
* ј̵̆
* ј̵̋
* ј̵́
* ј̵̈
* ј̶̉
* ј̶̀
* ј̶̃
* ј̶̂
* ј̶̄
* ј̶̇
* ј̶̊
* ј̶̌
* ј̶̒
* ј̶̆
* ј̶̋
* ј̶́
* ј̶̈
* ј̉
* ј̀
* ј̃
* ј̂
* ј̄
* ј̇
* ј̊
* ј̌
* ј̒
* ј̆
* ј̋
* ј́
* ј̈
* į̨̉
* į̨̀
* į̨̃
* į̨̂
* į̨̄
* į̨̇
* į̨̊
* į̨̌
* į̨̒
* į̨̆
* į̨̋
* į̨́
* į̨̈
* į̷̉
* į̷̀
* į̷̃
* į̷̂
* į̷̄
* į̷̇
* į̷̊
* į̷̌
* į̷̒
* į̷̆
* į̷̋
* į̷́
* į̷̈
* į̸̉
* į̸̀
* į̸̃
* į̸̂
* į̸̄
* į̸̇
* į̸̊
* į̸̌
* į̸̒
* į̸̆
* į̸̋
* į̸́
* į̸̈
* į̦̉
* į̦̀
* į̦̃
* į̦̂
* į̦̄
* į̦̇
* į̦̊
* į̦̌
* į̦̒
* į̦̆
* į̦̋
* į̦́
* į̦̈
* į̛̉
* į̛̀
* į̛̃
* į̛̂
* į̛̄
* į̛̇
* į̛̊
* į̛̌
* į̛̒
* į̛̆
* į̛̋
* į̛́
* į̛̈
* į̣̉
* į̣̀
* į̣̃
* į̣̂
* į̣̄
* į̣̇
* į̣̊
* į̣̌
* į̣̒
* į̣̆
* į̣̋
* į̣́
* į̣̈
* į̧̉
* į̧̀
* į̧̃
* į̧̂
* į̧̄
* į̧̇
* į̧̊
* į̧̌
* į̧̒
* į̧̆
* į̧̋
* į̧́
* į̧̈
* į̵̉
* į̵̀
* į̵̃
* į̵̂
* į̵̄
* į̵̇
* į̵̊
* į̵̌
* į̵̒
* į̵̆
* į̵̋
* į̵́
* į̵̈
* į̶̉
* į̶̀
* į̶̃
* į̶̂
* į̶̄
* į̶̇
* į̶̊
* į̶̌
* į̶̒
* į̶̆
* į̶̋
* į̶́
* į̶̈
* į̉
* į̇
* į̊
* į̒
* į̆
* į̋
* į̈ [code: soft-dotted]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. (googlefonts/vendor_id)</summary>
    <div>








- ⚠️ **WARN** OS/2 VendorID value 'VRCL' is not yet recognized.
If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
  
  

</div>
</details>


</div>
</details>


<details><summary>[11] fonts/Obvia/variable/Obvia[wght].ttf</summary>
<div>


<details>
    <summary>⚠️ <b>WARN</b> Check accent of Lcaron, dcaron, lcaron, tcaron (alt_caron)</summary>
    <div>








- ⚠️ **WARN** tcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. (contour_count)</summary>
    <div>








- ⚠️ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are
     inferred from the typical amounts of contours observed in a
     large collection of reference font families. The divergences
     listed below may simply indicate a significantly different
     design on some of your glyphs. On the other hand, some of these
     may flag actual bugs in the font such as glyphs mapped to an
     incorrect codepoint. Please consider reviewing the design and
     codepoint assignment of these to make sure they are correct.


    The following glyphs do not have the recommended number of contours:
* uni24FF (U+24FF): found 4, expected one of: {3}
* radical (U+221A): found 3, expected one of: {2, 1}
* partialdiff (U+2202): found 3, expected one of: {1, 2}
* arrowboth (U+2194): found 4, expected one of: {1, 3, 2}
* arrowupdn (U+2195): found 4, expected one of: {3, 1, 2} [code: contour-count]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Are there caret positions declared for every ligature? (ligature_carets)</summary>
    <div>








- ⚠️ **WARN** This font lacks caret positioning values for these ligature glyphs:

* U_I.dlig
* A_I.dlig [code: incomplete-caret-pos-data]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure variable fonts include an avar table. (mandatory_avar_table)</summary>
    <div>








- ⚠️ **WARN** The font does not include an avar table. [code: missing-avar]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. (math_signs_width)</summary>
    <div>








- ⚠️ **WARN** The most common width is 544 among a set of 13  math glyphs.
The following math glyphs have a different width, though:
width=540: divide, equal, notequal
width=558: plus
width=500: logicalnot
width=538: plusminus
width=502: multiply
width=523: approxequal
width=520: minus [code: width-outliers]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs (unreachable_glyphs)</summary>
    <div>








- ⚠️ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

* blackCircled [code: unreachable-glyphs]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Glyph names are all valid? (valid_glyphnames)</summary>
    <div>








- ⚠️ **WARN** The following glyph names are too long: "hyphen_hyphen_hyphen_greater.liga, periodcentered.loclCAT.case.ss08" [code: legacy-long-names]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Shapes languages in all GF glyphsets. (googlefonts/glyphsets/shape_languages)</summary>
    <div>








- ⚠️ **WARN** Warning language shaping:

| Message                                                               | Languages              |
|-----------------------------------------------------------------------|------------------------|
| Auxiliary orthography codepoints:                                     | * ca_Latn (Catalan)    |
|   The following auxiliary characters are missing from the font: Ŀ     |                        |
|   The following auxiliary characters are missing from the font: ŀ     |                        |
| Auxiliary orthography codepoints:                                     | * bg_Cyrl (Bulgarian)  |
|   Shaper didn't attach gravecomb to uni0430 when shaping the text 'а̀' |                        |
|   Shaper didn't attach gravecomb to uni043E when shaping the text 'о̀' |                        |
|   Shaper didn't attach gravecomb to uni0443 when shaping the text 'у̀' |                        |
|   Shaper didn't attach gravecomb to uni044A when shaping the text 'ъ̀' |                        |
|   Shaper didn't attach gravecomb to uni044E when shaping the text 'ю̀' |                        |
|   Shaper didn't attach gravecomb to uni044F when shaping the text 'я̀' |                        |
| Auxiliary orthography codepoints:                                     | * en_Latn (English)    |
|   The following auxiliary characters are missing from the font: ʻ     |                        |
| Auxiliary orthography codepoints:                                     | * fi_Latn (Finnish)    |
|   The following auxiliary characters are missing from the font: Ʒ     |                        |
|   The following auxiliary characters are missing from the font: Ǯ     |                        |
|   The following auxiliary characters are missing from the font: ʒ     |                        |
|   The following auxiliary characters are missing from the font: ǯ     |                        |
| Auxiliary orthography codepoints:                                     | * be_Cyrl (Belarusian) |
|   Shaper didn't attach acutecomb to uni0430 when shaping the text 'а́' |                        |
|   Shaper didn't attach acutecomb to uni0435 when shaping the text 'е́' |                        |
|   Shaper didn't attach acutecomb to uni0451 when shaping the text 'ё́' |                        |
|   Shaper didn't attach acutecomb to uni0456 when shaping the text 'і́' |                        |
|   Shaper didn't attach acutecomb to uni043E when shaping the text 'о́' |                        |
|   Shaper didn't attach acutecomb to uni0443 when shaping the text 'у́' |                        |
|   Shaper didn't attach acutecomb to uni044B when shaping the text 'ы́' |                        |
|   Shaper didn't attach acutecomb to uni044D when shaping the text 'э́' |                        |
|   Shaper didn't attach acutecomb to uni044E when shaping the text 'ю́' |                        |
|   Shaper didn't attach acutecomb to uni044F when shaping the text 'я́' |                        |
| Auxiliary orthography codepoints:                                     | * sr_Cyrl (Serbian)    |
|   Shaper didn't attach uni0302 to uni0430 when shaping the text 'а̂'   |                        |
|   Shaper didn't attach uni0302 to uni0435 when shaping the text 'е̂'   |                        |
|   Shaper didn't attach uni0302 to uni0438 when shaping the text 'и̂'   |                        |
|   Shaper didn't attach uni0302 to uni043E when shaping the text 'о̂'   |                        |
|   Shaper didn't attach uni0302 to uni0443 when shaping the text 'у̂'   |                        |
| Auxiliary orthography codepoints:                                     | * ru_Cyrl (Russian)    |
|   Shaper didn't attach acutecomb to uni0430 when shaping the text 'а́' |                        |
|   Shaper didn't attach acutecomb to uni0435 when shaping the text 'е́' |                        |
|   Shaper didn't attach acutecomb to uni0438 when shaping the text 'и́' |                        |
|   Shaper didn't attach acutecomb to uni043E when shaping the text 'о́' |                        |
|   Shaper didn't attach acutecomb to uni0443 when shaping the text 'у́' |                        |
|   Shaper didn't attach acutecomb to uni044B when shaping the text 'ы́' |                        |
|   Shaper didn't attach acutecomb to uni044D when shaping the text 'э́' |                        |
|   Shaper didn't attach acutecomb to uni044E when shaping the text 'ю́' |                        |
|   Shaper didn't attach acutecomb to uni044F when shaping the text 'я́' |                        |
| Auxiliary orthography codepoints:                                     | * de_Latn (German)     |
|   The following auxiliary characters are missing from the font: ſ     | * fr_Latn (French)     |
| Auxiliary orthography codepoints:                                     | * uk_Cyrl (Ukrainian)  |
|   Shaper didn't attach acutecomb to uni0430 when shaping the text 'а́' |                        |
|   Shaper didn't attach acutecomb to uni0435 when shaping the text 'е́' |                        |
|   Shaper didn't attach acutecomb to uni0454 when shaping the text 'є́' |                        |
|   Shaper didn't attach acutecomb to uni0438 when shaping the text 'и́' |                        |
|   Shaper didn't attach acutecomb to uni0456 when shaping the text 'і́' |                        |
|   Shaper didn't attach acutecomb to uni0457 when shaping the text 'ї́' |                        |
|   Shaper didn't attach acutecomb to uni043E when shaping the text 'о́' |                        |
|   Shaper didn't attach acutecomb to uni0443 when shaping the text 'у́' |                        |
|   Shaper didn't attach acutecomb to uni044E when shaping the text 'ю́' |                        |
|   Shaper didn't attach acutecomb to uni044F when shaping the text 'я́' |                        | [code: warning-language-shaping]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Font has correct separator glyphs? (googlefonts/separator_glyphs)</summary>
    <div>








- ⚠️ **WARN** The following separator glyphs are missing:

* U+2028
* U+2029 [code: missing-separator-glyphs]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that
replace the dot. (soft_dotted)</summary>
    <div>








- ⚠️ **WARN** The dot of soft dotted characters used in orthographies _must_ disappear in the following strings:

* і́
* į̄
* į̌
* į̀
* į̂
* į̃
* į́
* ị̄
* ị̀
* ị̂
* ị̃
* ị́The dot of soft dotted characters _should_ disappear in other cases, for example:

* і̣̋
* і̣̄
* і̣̌
* і̣̀
* і̣̂
* і̣̇
* і̣̃
* і̣̒
* і̣̆
* і̣̉
* і̣́
* і̣̊
* і̵̋
* і̵̄
* і̵̌
* і̵̀
* і̵̂
* і̵̇
* і̵̃
* і̵̒
* і̵̆
* і̵̉
* і̵́
* і̵̊
* і̦̋
* і̦̄
* і̦̌
* і̦̀
* і̦̂
* і̦̇
* і̦̃
* і̦̒
* і̦̆
* і̦̉
* і̦́
* і̦̊
* і̛̋
* і̛̄
* і̛̌
* і̛̀
* і̛̂
* і̛̇
* і̛̃
* і̛̒
* і̛̆
* і̛̉
* і̛́
* і̛̊
* і̨̋
* і̨̄
* і̨̌
* і̨̀
* і̨̂
* і̨̇
* і̨̃
* і̨̒
* і̨̆
* і̨̉
* і̨́
* і̨̊
* і̧̋
* і̧̄
* і̧̌
* і̧̀
* і̧̂
* і̧̇
* і̧̃
* і̧̒
* і̧̆
* і̧̉
* і̧́
* і̧̊
* і̶̋
* і̶̄
* і̶̌
* і̶̀
* і̶̂
* і̶̇
* і̶̃
* і̶̒
* і̶̆
* і̶̉
* і̶́
* і̶̊
* і̷̋
* і̷̄
* і̷̌
* і̷̀
* і̷̂
* і̷̇
* і̷̃
* і̷̒
* і̷̆
* і̷̉
* і̷́
* і̷̊
* і̸̋
* і̸̄
* і̸̌
* і̸̀
* і̸̂
* і̸̇
* і̸̃
* і̸̒
* і̸̆
* і̸̉
* і̸́
* і̸̊
* і̋
* і̄
* і̌
* і̀
* і̂
* і̇
* і̃
* і̒
* і̆
* і̉
* і̊
* ј̣̋
* ј̣̄
* ј̣̌
* ј̣̀
* ј̣̂
* ј̣̈
* ј̣̇
* ј̣̃
* ј̣̒
* ј̣̆
* ј̣̉
* ј̣́
* ј̣̊
* ј̵̋
* ј̵̄
* ј̵̌
* ј̵̀
* ј̵̂
* ј̵̈
* ј̵̇
* ј̵̃
* ј̵̒
* ј̵̆
* ј̵̉
* ј̵́
* ј̵̊
* ј̦̋
* ј̦̄
* ј̦̌
* ј̦̀
* ј̦̂
* ј̦̈
* ј̦̇
* ј̦̃
* ј̦̒
* ј̦̆
* ј̦̉
* ј̦́
* ј̦̊
* ј̛̋
* ј̛̄
* ј̛̌
* ј̛̀
* ј̛̂
* ј̛̈
* ј̛̇
* ј̛̃
* ј̛̒
* ј̛̆
* ј̛̉
* ј̛́
* ј̛̊
* ј̨̋
* ј̨̄
* ј̨̌
* ј̨̀
* ј̨̂
* ј̨̈
* ј̨̇
* ј̨̃
* ј̨̒
* ј̨̆
* ј̨̉
* ј̨́
* ј̨̊
* ј̧̋
* ј̧̄
* ј̧̌
* ј̧̀
* ј̧̂
* ј̧̈
* ј̧̇
* ј̧̃
* ј̧̒
* ј̧̆
* ј̧̉
* ј̧́
* ј̧̊
* ј̶̋
* ј̶̄
* ј̶̌
* ј̶̀
* ј̶̂
* ј̶̈
* ј̶̇
* ј̶̃
* ј̶̒
* ј̶̆
* ј̶̉
* ј̶́
* ј̶̊
* ј̷̋
* ј̷̄
* ј̷̌
* ј̷̀
* ј̷̂
* ј̷̈
* ј̷̇
* ј̷̃
* ј̷̒
* ј̷̆
* ј̷̉
* ј̷́
* ј̷̊
* ј̸̋
* ј̸̄
* ј̸̌
* ј̸̀
* ј̸̂
* ј̸̈
* ј̸̇
* ј̸̃
* ј̸̒
* ј̸̆
* ј̸̉
* ј̸́
* ј̸̊
* ј̋
* ј̄
* ј̌
* ј̀
* ј̂
* ј̈
* ј̇
* ј̃
* ј̒
* ј̆
* ј̉
* ј́
* ј̊
* į̣̋
* į̣̄
* į̣̌
* į̣̀
* į̣̂
* į̣̈
* į̣̇
* į̣̃
* į̣̒
* į̣̆
* į̣̉
* į̣́
* į̣̊
* į̵̋
* į̵̄
* į̵̌
* į̵̀
* į̵̂
* į̵̈
* į̵̇
* į̵̃
* į̵̒
* į̵̆
* į̵̉
* į̵́
* į̵̊
* į̦̋
* į̦̄
* į̦̌
* į̦̀
* į̦̂
* į̦̈
* į̦̇
* į̦̃
* į̦̒
* į̦̆
* į̦̉
* į̦́
* į̦̊
* į̛̋
* į̛̄
* į̛̌
* į̛̀
* į̛̂
* į̛̈
* į̛̇
* į̛̃
* į̛̒
* į̛̆
* į̛̉
* į̛́
* į̛̊
* į̨̋
* į̨̄
* į̨̌
* į̨̀
* į̨̂
* į̨̈
* į̨̇
* į̨̃
* į̨̒
* į̨̆
* į̨̉
* į̨́
* į̨̊
* į̧̋
* į̧̄
* į̧̌
* į̧̀
* į̧̂
* į̧̈
* į̧̇
* į̧̃
* į̧̒
* į̧̆
* į̧̉
* į̧́
* į̧̊
* į̶̋
* į̶̄
* į̶̌
* į̶̀
* į̶̂
* į̶̈
* į̶̇
* į̶̃
* į̶̒
* į̶̆
* į̶̉
* į̶́
* į̶̊
* į̷̋
* į̷̄
* į̷̌
* į̷̀
* į̷̂
* į̷̈
* į̷̇
* į̷̃
* į̷̒
* į̷̆
* į̷̉
* į̷́
* į̷̊
* į̸̋
* į̸̄
* į̸̌
* į̸̀
* į̸̂
* į̸̈
* į̸̇
* į̸̃
* į̸̒
* į̸̆
* į̸̉
* į̸́
* į̸̊
* į̋
* į̈
* į̇
* į̒
* į̆
* į̉
* į̊
* ị̣̋
* ị̣̄
* ị̣̌
* ị̣̀
* ị̣̂
* ị̣̈
* ị̣̇
* ị̣̃
* ị̣̒
* ị̣̆
* ị̣̉
* ị̣́
* ị̣̊
* ị̵̋
* ị̵̄
* ị̵̌
* ị̵̀
* ị̵̂
* ị̵̈
* ị̵̇
* ị̵̃
* ị̵̒
* ị̵̆
* ị̵̉
* ị̵́
* ị̵̊
* ị̦̋
* ị̦̄
* ị̦̌
* ị̦̀
* ị̦̂
* ị̦̈
* ị̦̇
* ị̦̃
* ị̦̒
* ị̦̆
* ị̦̉
* ị̦́
* ị̦̊
* ị̛̋
* ị̛̄
* ị̛̌
* ị̛̀
* ị̛̂
* ị̛̈
* ị̛̇
* ị̛̃
* ị̛̒
* ị̛̆
* ị̛̉
* ị̛́
* ị̛̊
* ị̧̋
* ị̧̄
* ị̧̌
* ị̧̀
* ị̧̂
* ị̧̈
* ị̧̇
* ị̧̃
* ị̧̒
* ị̧̆
* ị̧̉
* ị̧́
* ị̧̊
* ị̶̋
* ị̶̄
* ị̶̌
* ị̶̀
* ị̶̂
* ị̶̈
* ị̶̇
* ị̶̃
* ị̶̒
* ị̶̆
* ị̶̉
* ị̶́
* ị̶̊
* ị̷̋
* ị̷̄
* ị̷̌
* ị̷̀
* ị̷̂
* ị̷̈
* ị̷̇
* ị̷̃
* ị̷̒
* ị̷̆
* ị̷̉
* ị̷́
* ị̷̊
* ị̸̋
* ị̸̄
* ị̸̌
* ị̸̀
* ị̸̂
* ị̸̈
* ị̸̇
* ị̸̃
* ị̸̒
* ị̸̆
* ị̸̉
* ị̸́
* ị̸̊
* ị̋
* ị̌
* ị̈
* ị̇
* ị̒
* ị̆
* ị̉
* ị̊ [code: soft-dotted]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. (googlefonts/vendor_id)</summary>
    <div>








- ⚠️ **WARN** OS/2 VendorID value 'VRCL' is not yet recognized.
If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
  
  

</div>
</details>


</div>
</details>


<details><summary>[1] fonts/Obvia/variable</summary>
<div>


<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. (googlefonts/metadata/unreachable_subsetting)</summary>
    <div>








- ⚠️ **WARN** fonts/Obvia/variable/Obvia-Italic[wght].ttf: The following codepoints supported by the font are not covered by any subsets defined in the font's metadata file, and will never be served. You can solve this by either manually adding additional subset declarations to METADATA.pb, or by editing the glyphset definitions.

* U+02D8 BREVE: try adding one of: yi, canadian-aboriginal
* U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi
* U+02DB OGONEK: try adding one of: canadian-aboriginal, yi
* U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, cherokee, math, tifinagh
* U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic
* U+0307 COMBINING DOT ABOVE: try adding one of: duployan, todhri, syriac, math, canadian-aboriginal, old-permic, coptic, tai-le, tifinagh, malayalam, hebrew
* U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac
* U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage
* U+030C COMBINING CARON: try adding one of: tai-le, cherokee
* U+0312 COMBINING TURNED COMMA ABOVE: try adding math
* U+0326 COMBINING COMMA BELOW: try adding math
* U+0327 COMBINING CEDILLA: try adding math
* U+0338 COMBINING LONG SOLIDUS OVERLAY: try adding math
* U+039B GREEK CAPITAL LETTER LAMDA: try adding one of: elbasan, greek, math
* U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: elbasan, math, greek
* U+03BB GREEK SMALL LETTER LAMDA: try adding one of: greek, math
* U+03BC GREEK SMALL LETTER MU: try adding one of: greek, math
* U+03C0 GREEK SMALL LETTER PI: try adding one of: math, yi, greek
* U+03C9 GREEK SMALL LETTER OMEGA: try adding one of: greek, math
* U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai
* U+2021 DOUBLE DAGGER: try adding adlam
* U+2030 PER MILLE SIGN: try adding adlam
* U+2070 SUPERSCRIPT ZERO: try adding math
* U+2074 SUPERSCRIPT FOUR: try adding math
* U+2075 SUPERSCRIPT FIVE: try adding math
* U+2076 SUPERSCRIPT SIX: try adding math
* U+2077 SUPERSCRIPT SEVEN: try adding math
* U+2078 SUPERSCRIPT EIGHT: try adding math
* U+2079 SUPERSCRIPT NINE: try adding math
* U+2080 SUBSCRIPT ZERO: try adding math
* U+2081 SUBSCRIPT ONE: try adding math
* U+2082 SUBSCRIPT TWO: try adding math
* U+2083 SUBSCRIPT THREE: try adding math
* U+2084 SUBSCRIPT FOUR: try adding math
* U+2085 SUBSCRIPT FIVE: try adding math
* U+2086 SUBSCRIPT SIX: try adding math
* U+2087 SUBSCRIPT SEVEN: try adding math
* U+2088 SUBSCRIPT EIGHT: try adding math
* U+2089 SUBSCRIPT NINE: try adding math
* U+2117 SOUND RECORDING COPYRIGHT: try adding math
* U+2153 VULGAR FRACTION ONE THIRD: try adding symbols
* U+2154 VULGAR FRACTION TWO THIRDS: try adding symbols
* U+2155 VULGAR FRACTION ONE FIFTH: try adding symbols
* U+215B VULGAR FRACTION ONE EIGHTH: try adding symbols
* U+215C VULGAR FRACTION THREE EIGHTHS: try adding symbols
* U+215D VULGAR FRACTION FIVE EIGHTHS: try adding symbols
* U+215E VULGAR FRACTION SEVEN EIGHTHS: try adding symbols
* U+2190 LEFTWARDS ARROW: try adding one of: math, symbols
* U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols
* U+2194 LEFT RIGHT ARROW: try adding one of: symbols, math
* U+2195 UP DOWN ARROW: try adding one of: symbols, math
* U+2196 NORTH WEST ARROW: try adding one of: symbols, math
* U+2197 NORTH EAST ARROW: try adding one of: symbols, math
* U+2198 SOUTH EAST ARROW: try adding one of: symbols, math
* U+2199 SOUTH WEST ARROW: try adding one of: math, symbols
* U+219D RIGHTWARDS WAVE ARROW: try adding math
* U+21A9 LEFTWARDS ARROW WITH HOOK: try adding math
* U+21AA RIGHTWARDS ARROW WITH HOOK: try adding math
* U+21B0 UPWARDS ARROW WITH TIP LEFTWARDS: try adding math
* U+21B1 UPWARDS ARROW WITH TIP RIGHTWARDS: try adding math
* U+21B3 DOWNWARDS ARROW WITH TIP RIGHTWARDS: try adding math
* U+21B4 RIGHTWARDS ARROW WITH CORNER DOWNWARDS: try adding math
* U+21B5 DOWNWARDS ARROW WITH CORNER LEFTWARDS: try adding math
* U+21E4 LEFTWARDS ARROW TO BAR: try adding math
* U+21E5 RIGHTWARDS ARROW TO BAR: try adding math
* U+21E7 UPWARDS WHITE ARROW: try adding symbols
* U+2202 PARTIAL DIFFERENTIAL: try adding math
* U+2206 INCREMENT: try adding math
* U+220F N-ARY PRODUCT: try adding math
* U+2211 N-ARY SUMMATION: try adding math
* U+221A SQUARE ROOT: try adding math
* U+221E INFINITY: try adding math
* U+222B INTEGRAL: try adding math
* U+2236 RATIO: try adding math
* U+2248 ALMOST EQUAL TO: try adding math
* U+2260 NOT EQUAL TO: try adding math
* U+2264 LESS-THAN OR EQUAL TO: try adding math
* U+2265 GREATER-THAN OR EQUAL TO: try adding math
* U+2460 CIRCLED DIGIT ONE: try adding one of: symbols, yi, mongolian
* U+2461 CIRCLED DIGIT TWO: try adding one of: mongolian, symbols, yi
* U+2462 CIRCLED DIGIT THREE: try adding one of: mongolian, yi, symbols
* U+2463 CIRCLED DIGIT FOUR: try adding one of: yi, symbols, mongolian
* U+2464 CIRCLED DIGIT FIVE: try adding one of: symbols, mongolian, yi
* U+2465 CIRCLED DIGIT SIX: try adding one of: symbols, yi, mongolian
* U+2466 CIRCLED DIGIT SEVEN: try adding one of: symbols, mongolian, yi
* U+2467 CIRCLED DIGIT EIGHT: try adding one of: mongolian, symbols, yi
* U+2468 CIRCLED DIGIT NINE: try adding one of: yi, mongolian, symbols
* U+24EA CIRCLED DIGIT ZERO: try adding symbols
* U+24FF NEGATIVE CIRCLED DIGIT ZERO: try adding symbols
* U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols
* U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: math, symbols
* U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols
* U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: symbols, math
* U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols
* U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: math, symbols
* U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols
* U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: symbols, math
* U+25CA LOZENGE: try adding one of: math, symbols
* U+25CB WHITE CIRCLE: try adding symbols
* U+25CC DOTTED CIRCLE: try adding one of: grantha, thai, buhid, tagalog, yi, hebrew, mende-kikakui, phags-pa, wancho, khmer, tirhuta, balinese, chakma, meetei-mayek, pahawh-hmong, batak, miao, syloti-nagri, ahom, caucasian-albanian, sogdian, gujarati, hanunoo, old-permic, elbasan, mongolian, bhaiksuki, soyombo, dogra, psalter-pahlavi, siddham, mahajani, kayah-li, syriac, tai-le, tamil, telugu, nko, khojki, sharada, takri, armenian, tifinagh, oriya, bengali, math, javanese, gunjala-gondi, hanifi-rohingya, coptic, duployan, gurmukhi, adlam, kannada, kharoshthi, lepcha, modi, mandaic, brahmi, myanmar, rejang, canadian-aboriginal, sundanese, khudawadi, manichaean, saurashtra, tagbanwa, limbu, tibetan, zanabazar-square, music, tai-viet, kaithi, warang-citi, osage, bassa-vah, buginese, newa, masaram-gondi, symbols, sinhala, cham, tai-tham, malayalam, new-tai-lue, thaana, lao, devanagari, marchen
* U+25CF BLACK CIRCLE: try adding symbols
* U+2639 WHITE FROWNING FACE: try adding symbols
* U+263A WHITE SMILING FACE: try adding symbols
* U+2776 DINGBAT NEGATIVE CIRCLED DIGIT ONE: try adding symbols
* U+2777 DINGBAT NEGATIVE CIRCLED DIGIT TWO: try adding symbols
* U+2778 DINGBAT NEGATIVE CIRCLED DIGIT THREE: try adding symbols
* U+2779 DINGBAT NEGATIVE CIRCLED DIGIT FOUR: try adding symbols
* U+277A DINGBAT NEGATIVE CIRCLED DIGIT FIVE: try adding symbols
* U+277B DINGBAT NEGATIVE CIRCLED DIGIT SIX: try adding symbols
* U+277C DINGBAT NEGATIVE CIRCLED DIGIT SEVEN: try adding symbols
* U+277D DINGBAT NEGATIVE CIRCLED DIGIT EIGHT: try adding symbols
* U+277E DINGBAT NEGATIVE CIRCLED DIGIT NINE: try adding symbols
* U+301C WAVE DASH: try adding japanese

Or you can add the above codepoints to one of the subsets supported by the font: cyrillic-ext, cyrillic, latin-ext, latin, vietnamese [code: unreachable-subsetting]
  
  


- ⚠️ **WARN** fonts/Obvia/variable/Obvia[wght].ttf: The following codepoints supported by the font are not covered by any subsets defined in the font's metadata file, and will never be served. You can solve this by either manually adding additional subset declarations to METADATA.pb, or by editing the glyphset definitions.

* U+02D8 BREVE: try adding one of: yi, canadian-aboriginal
* U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi
* U+02DB OGONEK: try adding one of: canadian-aboriginal, yi
* U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, cherokee, math, tifinagh
* U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic
* U+0307 COMBINING DOT ABOVE: try adding one of: duployan, todhri, syriac, math, canadian-aboriginal, old-permic, coptic, tai-le, tifinagh, malayalam, hebrew
* U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac
* U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage
* U+030C COMBINING CARON: try adding one of: tai-le, cherokee
* U+0312 COMBINING TURNED COMMA ABOVE: try adding math
* U+0326 COMBINING COMMA BELOW: try adding math
* U+0327 COMBINING CEDILLA: try adding math
* U+0338 COMBINING LONG SOLIDUS OVERLAY: try adding math
* U+039B GREEK CAPITAL LETTER LAMDA: try adding one of: elbasan, greek, math
* U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: elbasan, math, greek
* U+03BB GREEK SMALL LETTER LAMDA: try adding one of: greek, math
* U+03BC GREEK SMALL LETTER MU: try adding one of: greek, math
* U+03C0 GREEK SMALL LETTER PI: try adding one of: math, yi, greek
* U+03C9 GREEK SMALL LETTER OMEGA: try adding one of: greek, math
* U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai
* U+2021 DOUBLE DAGGER: try adding adlam
* U+2030 PER MILLE SIGN: try adding adlam
* U+2070 SUPERSCRIPT ZERO: try adding math
* U+2074 SUPERSCRIPT FOUR: try adding math
* U+2075 SUPERSCRIPT FIVE: try adding math
* U+2076 SUPERSCRIPT SIX: try adding math
* U+2077 SUPERSCRIPT SEVEN: try adding math
* U+2078 SUPERSCRIPT EIGHT: try adding math
* U+2079 SUPERSCRIPT NINE: try adding math
* U+2080 SUBSCRIPT ZERO: try adding math
* U+2081 SUBSCRIPT ONE: try adding math
* U+2082 SUBSCRIPT TWO: try adding math
* U+2083 SUBSCRIPT THREE: try adding math
* U+2084 SUBSCRIPT FOUR: try adding math
* U+2085 SUBSCRIPT FIVE: try adding math
* U+2086 SUBSCRIPT SIX: try adding math
* U+2087 SUBSCRIPT SEVEN: try adding math
* U+2088 SUBSCRIPT EIGHT: try adding math
* U+2089 SUBSCRIPT NINE: try adding math
* U+2117 SOUND RECORDING COPYRIGHT: try adding math
* U+2153 VULGAR FRACTION ONE THIRD: try adding symbols
* U+2154 VULGAR FRACTION TWO THIRDS: try adding symbols
* U+2155 VULGAR FRACTION ONE FIFTH: try adding symbols
* U+215B VULGAR FRACTION ONE EIGHTH: try adding symbols
* U+215C VULGAR FRACTION THREE EIGHTHS: try adding symbols
* U+215D VULGAR FRACTION FIVE EIGHTHS: try adding symbols
* U+215E VULGAR FRACTION SEVEN EIGHTHS: try adding symbols
* U+2190 LEFTWARDS ARROW: try adding one of: math, symbols
* U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols
* U+2194 LEFT RIGHT ARROW: try adding one of: symbols, math
* U+2195 UP DOWN ARROW: try adding one of: symbols, math
* U+2196 NORTH WEST ARROW: try adding one of: symbols, math
* U+2197 NORTH EAST ARROW: try adding one of: symbols, math
* U+2198 SOUTH EAST ARROW: try adding one of: symbols, math
* U+2199 SOUTH WEST ARROW: try adding one of: math, symbols
* U+219D RIGHTWARDS WAVE ARROW: try adding math
* U+21A9 LEFTWARDS ARROW WITH HOOK: try adding math
* U+21AA RIGHTWARDS ARROW WITH HOOK: try adding math
* U+21B0 UPWARDS ARROW WITH TIP LEFTWARDS: try adding math
* U+21B1 UPWARDS ARROW WITH TIP RIGHTWARDS: try adding math
* U+21B3 DOWNWARDS ARROW WITH TIP RIGHTWARDS: try adding math
* U+21B4 RIGHTWARDS ARROW WITH CORNER DOWNWARDS: try adding math
* U+21B5 DOWNWARDS ARROW WITH CORNER LEFTWARDS: try adding math
* U+21E4 LEFTWARDS ARROW TO BAR: try adding math
* U+21E5 RIGHTWARDS ARROW TO BAR: try adding math
* U+21E7 UPWARDS WHITE ARROW: try adding symbols
* U+2202 PARTIAL DIFFERENTIAL: try adding math
* U+2206 INCREMENT: try adding math
* U+220F N-ARY PRODUCT: try adding math
* U+2211 N-ARY SUMMATION: try adding math
* U+221A SQUARE ROOT: try adding math
* U+221E INFINITY: try adding math
* U+222B INTEGRAL: try adding math
* U+2236 RATIO: try adding math
* U+2248 ALMOST EQUAL TO: try adding math
* U+2260 NOT EQUAL TO: try adding math
* U+2264 LESS-THAN OR EQUAL TO: try adding math
* U+2265 GREATER-THAN OR EQUAL TO: try adding math
* U+2460 CIRCLED DIGIT ONE: try adding one of: symbols, yi, mongolian
* U+2461 CIRCLED DIGIT TWO: try adding one of: mongolian, symbols, yi
* U+2462 CIRCLED DIGIT THREE: try adding one of: mongolian, yi, symbols
* U+2463 CIRCLED DIGIT FOUR: try adding one of: yi, symbols, mongolian
* U+2464 CIRCLED DIGIT FIVE: try adding one of: symbols, mongolian, yi
* U+2465 CIRCLED DIGIT SIX: try adding one of: symbols, yi, mongolian
* U+2466 CIRCLED DIGIT SEVEN: try adding one of: symbols, mongolian, yi
* U+2467 CIRCLED DIGIT EIGHT: try adding one of: mongolian, symbols, yi
* U+2468 CIRCLED DIGIT NINE: try adding one of: yi, mongolian, symbols
* U+24EA CIRCLED DIGIT ZERO: try adding symbols
* U+24FF NEGATIVE CIRCLED DIGIT ZERO: try adding symbols
* U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols
* U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: math, symbols
* U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols
* U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: symbols, math
* U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols
* U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: math, symbols
* U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols
* U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: symbols, math
* U+25CA LOZENGE: try adding one of: math, symbols
* U+25CB WHITE CIRCLE: try adding symbols
* U+25CC DOTTED CIRCLE: try adding one of: grantha, thai, buhid, tagalog, yi, hebrew, mende-kikakui, phags-pa, wancho, khmer, tirhuta, balinese, chakma, meetei-mayek, pahawh-hmong, batak, miao, syloti-nagri, ahom, caucasian-albanian, sogdian, gujarati, hanunoo, old-permic, elbasan, mongolian, bhaiksuki, soyombo, dogra, psalter-pahlavi, siddham, mahajani, kayah-li, syriac, tai-le, tamil, telugu, nko, khojki, sharada, takri, armenian, tifinagh, oriya, bengali, math, javanese, gunjala-gondi, hanifi-rohingya, coptic, duployan, gurmukhi, adlam, kannada, kharoshthi, lepcha, modi, mandaic, brahmi, myanmar, rejang, canadian-aboriginal, sundanese, khudawadi, manichaean, saurashtra, tagbanwa, limbu, tibetan, zanabazar-square, music, tai-viet, kaithi, warang-citi, osage, bassa-vah, buginese, newa, masaram-gondi, symbols, sinhala, cham, tai-tham, malayalam, new-tai-lue, thaana, lao, devanagari, marchen
* U+25CF BLACK CIRCLE: try adding symbols
* U+2639 WHITE FROWNING FACE: try adding symbols
* U+263A WHITE SMILING FACE: try adding symbols
* U+2776 DINGBAT NEGATIVE CIRCLED DIGIT ONE: try adding symbols
* U+2777 DINGBAT NEGATIVE CIRCLED DIGIT TWO: try adding symbols
* U+2778 DINGBAT NEGATIVE CIRCLED DIGIT THREE: try adding symbols
* U+2779 DINGBAT NEGATIVE CIRCLED DIGIT FOUR: try adding symbols
* U+277A DINGBAT NEGATIVE CIRCLED DIGIT FIVE: try adding symbols
* U+277B DINGBAT NEGATIVE CIRCLED DIGIT SIX: try adding symbols
* U+277C DINGBAT NEGATIVE CIRCLED DIGIT SEVEN: try adding symbols
* U+277D DINGBAT NEGATIVE CIRCLED DIGIT EIGHT: try adding symbols
* U+277E DINGBAT NEGATIVE CIRCLED DIGIT NINE: try adding symbols
* U+301C WAVE DASH: try adding japanese

Or you can add the above codepoints to one of the subsets supported by the font: cyrillic-ext, cyrillic, latin-ext, latin, vietnamese [code: unreachable-subsetting]
  
  

</div>
</details>


</div>
</details>






### Summary

| 💥 ERROR | ⚠️ WARN | ℹ️ INFO | ✅ PASS | ⏩ SKIP | 
| ---|---|---|---|---|
| 2 | 24 | 14 | 219 | 66 | 
| 1% | 7% | 4% | 68% | 20% | 



