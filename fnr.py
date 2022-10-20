import pathlib

def update_bs_js():
    for p in pathlib.Path("C:/Users/Admin/Documents/GitHub/opensourcegisdata/v1").rglob("*.html"):
        print(p)
        text = p.read_text()
        text = text.replace('<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>', '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>')
        p.write_text(text)

def find_replace(path, find, replace):
    for p in pathlib.Path(path).rglob("*.html"):
        print(p)
        text = p.read_text()
        text = text.replace(find, replace)
        p.write_text(text)

def replace_state_menus():
    old_state_menu = """
                        <div class="card mb-4">
                            <div class="card-header">Categories</div>
                            <div class="card-body">
                                <div class="row">
                                    <div class="col-sm-6">
                                        <ul class="list-unstyled mb-0">
                                            <li><a href="./index.html">State Sources</a></li>
                                            <li><a href="#!">US National Sources</a></li>
                                            <li><a href="#!">QGIS</a></li>
                                        </ul>
                                    </div>
                                    <div class="col-sm-6">
                                        <ul class="list-unstyled mb-0">
                                            <li><a href="#!">Resources</a></li>
                                            <li><a href="#!">Tutorials</a></li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
    """
    new_state_menu = """
                        <div class="card mb-4">
                            <div class="card-header">Categories</div>
                            <div class="card-body">
                                <div class="row">
                                    <div class="col-sm-6">
                                        <ul class="list-unstyled mb-0">
                                            <li><a href="./index.html">US Sources</a></li>
                                            <li><a href="../us-federal/index.html">US Federal Sources</a></li>
                                            <li><a href="../international/index.html">International</a></li>
                                        </ul>
                                    </div>
                                    <div class="col-sm-6">
                                        <ul class="list-unstyled mb-0">
                                            <li><a href="../software/index.html">Software</a></li>
                                            <li><a href="../resources/index.html">Resources</a></li>
                                            <li><a href="../tutorials/index.html">Tutorials</a></li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
    """

    find_replace("C:/Users/Admin/Documents/GitHub/opensourcegisdata/v1/state", old_state_menu, new_state_menu)