# spaCy custom extensions

When using [spacypdfreader.pdf_reader][] custom attributes and methods are added to spacy objects.

## `spacy.Doc` 

### Extension attributes

| Extension   | Type   | Description   |
| ------ | ------ | ------ |
| `doc._.pdf_file_name` | `str` | The file name of the PDF document. |
| `doc._.first_page` | `int` | The first page number of the PDF. |
| `doc._.last_page` | `int` | The last page number of the PDF. |
| `doc._.page_range` | `(int, int)` | The range of pages from the PDF. |
| `doc._.page(int)` | `int` | Return the span of text related to the page. |

### Extension methods

#### `Doc._.page`

**Parameters:**

| Name          | Type  | Description                                  | Default    |
| ------------- | ----- | -------------------------------------------- | ---------- |
| `page_number` | `int` | The PDF page number of the doc to filter on. | *required* |

**Returns:**

| Type         | Description                                              |
| ------------ | -------------------------------------------------------- |
| `spacy.Span` | The span of text from the corresponding PDF page number. |

## `spacy.Token`

### Extension attributes

| Extension   | Type   | Description   |
| ------ | ------ | ------ |
| `token._.page_number` |  `int`      | The PDF page number in which the token was extracted from. The first page is `1`.      |