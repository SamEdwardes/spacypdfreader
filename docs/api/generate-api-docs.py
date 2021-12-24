from lazydocs import generate_docs


generate_docs(
    paths=["spacypdfreader"],
    output_path="./website/docs/api",
    src_base_url="https://github.com/SamEdwardes/spaCyPDFreader/blob/mkdocs-website/",
    ignored_modules=["console"],
    overview_file="overview.md",
)