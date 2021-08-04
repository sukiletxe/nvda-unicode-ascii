# Unicode ASCII (convert Unicode characters to ASCII)

## Introduction

This addon aims to solve the problem with mathematical alphanumeric characters, which, among other things, are now used for decorative purposes because they look cool on social networks, in addition to them being used with their originally thought use. The addon converts the characters you pass to it to a close ASCII representation, so it may be used to transliterate any other symbol. Unfortunately,  the results won't always be perfect or good because sometimes decorative characters work on similarity with the original character, not actual meaning.

Note: This addon may not transliterate Japanese and Chinese text (among others) correctly, as the library it uses doesn't have any way to guess the text's language. Also, if it fails to transliterate a character it will preserve it, so the result may not always be in ASCII. 

## Usage

* Press NVDA+Ctrl+N to decode the selected text, press it twice to copy the result to the clipboard.
* Press CTRL+Shift+NVDA+N to decode the text of the clipboard, press it twice to copy the result.

These shortcuts can be changed in the input gestures dialog, in the unicodeAscii category.

## Changelog

### 1.0.1

* Now text which cannot be converted will be ignored instead of replaced by question marks.

### 1.0

* First version.

## Thanks

* Jesús Pavón for the idea.
* Javi Domínguez for [FEN Reader][FEN]. Most of this add-on's code is based on it.
* Sean M. Burke for `Text::Unidecode` and Tomaž Šolc for [Unidecode].
* [Nikola] for being great and using Unidecode (that's where I found it).

[FEN]: https://github.com/javidominguez/FenReader/
[Unidecode]: https://github.com/avian2/unidecode
[Nikola]: https://getnikola.com/avian2/unidecode