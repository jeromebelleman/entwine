# NAME

entwine – generate web site

# SYNOPSIS

See **entwine -h**.

# PANDOC OPTIONS

You can set Pandoc variables in a YAML front matter, as well as pass options
to Pandoc in its `options` dictionary:

```yaml
title: Page Title
description: >
    This is a description of the page, which may be written in multiple
    lines, should the contents require it.
date: 12 Nov 2016

options:
    css: ../styles.css
    toc: true
    number-sections: true
```

# RUNNING PYTHON FROM TEMPLATES

You can do so between the `{{` and `}}` tags, either in a single or multiple
lines. You can also refer to variables set in the front matter.  The `outdir`
variables is also provided, and the `os` and `entwinelib` modules imported:

```
{{
with open('/etc/issue') as fhl:
    linux = fhl.read()
}}

This page entitled "{{ print meta['title'] }}" was generated on
{{ print linux.strip() }} into the {{ print outdir }} directory.  Available
functions are: <pre>{{ print dir(entwinelib) }}</pre>.
```

Python blocks are also useful to comment out with `#` anything you wouldn't
want your visitors to see if you used `<!-- -->`. Likewise, it's a neat way to
specify Vim modelines, e.g.:

```
{{
# vim: nowrap virtualedit=all
}}
```

You can define other functions. Functions defined in a given `{{` `}}`
block is visible to other blocks in the file too.
