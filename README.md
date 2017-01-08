# NAME

entwine – generate web site

# SYNOPSIS

See **entwine -h**.

# PANDOC OPTIONS

You can pass optional arguments to Pandoc in an HTML comment in the first
line of the file. Note that newlines aren't supported and that everything
must stay in one line. Typically useful ones are:

  - `include-in-header=styles.css` to specify the location of a file
    containing a style tag, relative to the location of the page.
    More on this below.
  - `variable=desc:"Description of my page"` to set Pandoc variables,
    namely the `desc` one which contains the meta description of the page
    in the template we normally use. I think Google calls a good description
    one that's at least 150-characters long.
  - `toc` and `number-sections` to add a table of contents and number sections.

# STYLES

With a Pandoc argument like `include-in-header=styles.css`, you can include
a style tag by specifying the location of a file containing a whole style
tag, like:

```
<style type="text/css">
h1 {{
    float: none;
    clear: both;
}}
</style>
```

Note that it's not the same as specifying a style sheet as you normally
would in HTML.

# RUNNING PYTHON FROM TEMPLATES

You can do so between `<%` and `%>` tags. Available attributes in scope
are the `os` module, the `__params__` dictionary.

Note that you can set `__params__['updated']` to any literal string. It's
also typically formatted as `%d %b %Y`, although you could take the liberty
of formatting it `%b %Y`. You can also set it to the empty string to not
display the last change time on the page.

Python blocks are also useful to comment out with `#` anything you wouldn't
your visitors to see if you used `<!-- -->`. Likewise, it's a neat way to
specify Vim modelines, e.g.:

```
<%
# vim: nowrap virtualedit=all
%>
```

You can define other functions. Functions defined in a given `<%` `%>`
block is visible to other blocks in the file too.
