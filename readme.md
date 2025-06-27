# Unicode ASCII (convert Unicode characters to ASCII)

## Introduction

This addon aims to solve the problem with mathematical alphanumeric characters, which, among other things, are now used for decorative purposes because they look cool on social networks, in addition to them being used with their originally thought use. The addon converts the characters you pass to it to a close ASCII representation using the [Unidecode] library, so it may be used to transliterate any other symbol. Unfortunately,  the results won't always be perfect or good because sometimes decorative characters work on similarity with the original character, not actual meaning.

Note: This addon may not transliterate Japanese and Chinese text (among others) correctly, as the library it uses doesn't have any way to guess the text's language. Also, if it fails to transliterate a character it will preserve it, so the result may not always be in ASCII. 

## Usage

* Press NVDA+Ctrl+N to decode the text of the clipboard or the selected text (in that order of searching), press it twice to copy the result to the clipboard.
* Press CTRL+Shift+NVDA+N to decode the text of the clipboard or the selected text (in that order) and add them as pattern and replacement to the default dictionary (useful if you find a string of text frequently).

These shortcuts can be changed in the input gestures dialog, in the unicodeAscii category.

## What to do when transliteration fails

You can use [the Character information add-on][charinfo] to retrieve more information about a character, and possibly add it to the punctuation and symbols dialog or your NVDA dictionary.

## Changelog

See [Unidecode's changelog][unich] for the library's changelog.

### Version 1.5

* Compatibility with NVDA 2025.x.

### Version 1.4



* Update Unidecode to 1.3.8.
* Compatibility with NVDA 2024.x.

### Version 1.3

* Compatibility with NVDA 2023.x.

### Version 1.2

* Compatibility with NVDA 2022.x.

### Version 1.1.3

* Cleaned addon path after importing everything.

### Version 1.1.2

* Add notes for translations.

### Version 1.1.1

* Now an error will be reported when there is no text to decode.

### Version 1.1

* Added possibility to add a string and its decoded counterpart to the default dictionary, changed shortcuts.

### Version 1.0.1

* Now text which cannot be converted will be kept instead of replaced by question marks.

### Version 1.0

* First version.

## Thanks

* Jesús Pavón for the idea.
* Javi Domínguez for [FEN Reader][FEN]. Most of this add-on's code is based on it (the skeleton of the add-on and the getSelection function).
* Sean M. Burke for `Text::Unidecode` and Tomaž Šolc for [Unidecode].
* [Nikola] for being great and using Unidecode (that's where I found it).

[FEN]: https://github.com/javidominguez/FenReader/
[Unidecode]: https://github.com/avian2/unidecode
[Nikola]: https://getnikola.com/avian2/unidecode
[charinfo]: https://addons.nvda-project.org/addons/charInfo.en.html
[unich]: https://github.com/avian2/unidecode/blob/master/ChangeLog