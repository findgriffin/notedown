notedown
========

Easy notetaking for maths, science and everything else.

The Problem
===========

Maths is hard, but trying to take notes that include mathematical symbols on
any kind of computing device is harder. The status quo is that we have:

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
Markdown is a widely 'standard' that can be rendered to html or other formats.
It is used by millions of people on sites like reddit, stackoverflow, this
description box etc.

Notedown is an extension of markdown that will allow the integration of
mathematical symbols in an intuitive and simple manner.

Anybody who wants to contribute is most welcome.

Syntax
======
The aims of notedown's mathematics syntax are to

1. Use existing conventions wherever possible
1. Be intuitive, the notedown source should look as much as possible like the
   rendered output. 
1. Not intrude unexpectedly. A user should not be surprised by escape
   characters like `\` or `$` or `&`. 

Notedown documents should be valid markdown (possibly github flavoured
markdown) documents with the additional rules that:

1. Words with any of the characters `<>~=/*+_^` *in the middle of the word*
   will be rendered using notedown's mathematics syntax rules.  
1. The above rule does not apply for words inside code blocks (i.e. backticks
   or indented)
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
 * etcetera
 * Notedown supports order of operations using braces `{}`, brackets `[]` and
   parenthesis `()`

Implementation plan
===================
Obviously the variety and breadth of mathematical symbols makes it difficult or
impossible to support everything. To support everything would require a more
complex syntax and we would end up with something like LaTeX, which would
completely defeat the point!. To that end the current plan is to start with all
the mathematical notation needed by a high school student. That means basic
maths, chemistry, calculus etc. Once that is complete then the goal will be to
move out to support both younger and older audiences, these audiences have
somewhat opposite requirements:

  * Young children don't need complex notation (eg greek letters) but ease of
    use and simplicity is most important
  * Older users eg. university students need more complex kinds of notation.
    One possibility is to have different 'modes' when inside fenced code
    blocks, eg.  chemistry, biology, physics, nuclear physics etc. 
  * For the pathological case I propose to support a latex mode. 

Examples
=======
 
 * 2+2=4
 * 8/2
 * F=ma
 * V/R=i
 * a^2+b^2=c^2
 * t'=t(1/sqrt(1-v^2/c^2))
 * F=(1/2)mv^2 F=mv^2/2
 * F=G(m_1m_2/d^2)
 * \deltaS>=0
 * e=mc^2
 * H_2O
 * G_(\mu\nu)=8\piG(T_(\munu)+rho_(\LAMBDA)g_(\mu\nu))
 * 
