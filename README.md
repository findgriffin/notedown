notedown
========

Easy notetaking for maths, science and everything else.

The Problem
===========

Maths is hard, but trying to take notes that include mathematical symbols on any kind of computing device is harder. The status quo is that we have:

 * Equation editors, eg. MS Office, these are slow due to their 'point and
click' design. If the user has to take their fingers off the keyboard then they
will not be able to write fast enough. 

* Quasi standards like using _ for subscript and ^ for superscript, for times
and / for division... These largely work but only a limited subset of
mathematical symbols are supported and standards are ad-hock, additionally
these kinds of things are mostly only used by already computer/mathematically
literate people.  

* LaTex (or html and friends). You can do pretty much anything you want in
LaTeX but it's complicated to install, harder to learn and even harder to type
quickly. Commonly used symbols like $ and & are escape characters creating an
enormous mental strain when working quickly.

The Solution
============
Markdown is a widely 'standard' that can be rendered to html or other formats. It is used by millions of people on sites like reddit, stackoverflow, this description box etc.

Notedown is an extension of markdown that will allow the integration of mathematical symbols in an intuitive and simple manner.

Anybody who wants to contribute is most welcome.

Syntax
======
The aims of notedown's mathematics syntax are to

1. Use existing conventions wherever possible
1. Be intuitive, the notedown source should look as much as possible like the rendered output. 
1. Not intrude unexpectedly. A user should not be surprised by escape characters like `\` or `$` or `&`. 

Notedown documents should be valid markdown (possibly github flavoured
markdown) documents with the additional rules that:

1. Words with any of the characters `<>~=/*+_^` *in the middle of the word*
will be rendered using notedown's mathematics syntax rules.  
1. The above rule does not apply for words inside code blocks (i.e. backticks or indented)
1. Notedown will support github style fenced code blocks. 
1. Tables, the syntax for tables is tbd.

Mathematics syntax rules
========================
 * * times 
 * / fraction / division
 * > greater than
 * >=| greater than or equal to
 * < less than
 * <=| less than or equal to
 * Notedown supports order of operations using braces `{}`, brackets `[]` and parenthesis `()`
 * etcetera

Examples
=======

 * 2+2=4
 * 8/2
 * F=ma
 * V/R=i
 * F=(1/2)mv^2 F=mv^2/2
 * e=mc^2
 * H_2O
