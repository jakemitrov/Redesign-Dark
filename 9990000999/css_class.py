def inject_css_class(state: bool, html: str):
    if state:
        javascript = """
            function add_anki_redesign_class(){
                current_classes = document.body.className;
                if(current_classes.indexOf("anki_redesign") == -1)
                {
                    document.body.className += " anki_redesign";
                }
            }
            // explanation of setTimeout use:
            // callback defined in _showQuestion of reviewer.js would otherwise overwrite
            // the newly set body class; in order to prevent that the function execution
            // is being placed on the end of execution queue (hence time = 0)
            setTimeout(add_anki_redesign_class, 0)
            """
    else:
        javascript = """
            function remove_anki_redesign_class(){
                current_classes = document.body.className;
                if(current_classes.indexOf("anki_redesign") != -1)
                {
                    document.body.className = current_classes.replace("anki_redesign","");
                }
            }
            setTimeout(remove_anki_redesign_class, 0)
            """
    # script on the beginning of the HTML so it will always be
    # before any user-defined, potentially malformed HTML
    html = f"<script>{javascript}</script>" + html
    return html
