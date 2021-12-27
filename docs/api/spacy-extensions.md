### Extensions

When using `spacypdfreader.pdf_reader` a `spacy.tokens.Doc` object with custom extensions is returned.

| Extension   | Type   | Description   | Default   |
| ------ | ------ | ------ | ------ |
| `token._.page_number` |  `int`      | The PDF page number in which the token was extracted from. The first page is `1`.      |  `None`      |