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

def find_replace_json(path, find, replace):
    for p in pathlib.Path(path).rglob("*.json"):
        print(p)
        text = p.read_text()
        text = text.replace(find, replace)
        p.write_text(text)

def replace_side_menu():
    old_menu = """
                <div class="col-lg-4">
                    <!-- Categories widget-->
                    <div class="card mb-4">
                        <div class="card-header">Categories</div>
                        <div class="card-body">
                            <div class="row">
                                <div class="col-sm-6">
                                    <ul class="list-unstyled mb-0">
                                        <li><a href="../state/index.html">US Sources</a></li>
                                        <li><a href="./index.html">US Federal Sources</a></li>
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
                </div>
    """
    newmenu = " "
    find_replace("C:/Users/Admin/Documents/GitHub/opensourcegisdata/v3-v2-merge/state", old_menu, newmenu)
    find_replace("C:/Users/Admin/Documents/GitHub/opensourcegisdata/v3-v2-merge/us-federal", old_menu, newmenu)

def columspace():
    old = """<div class="col-lg-8" data-bs-spy="scroll" id="scroll-nav">
    """
    new = """<div class="col-lg-12" data-bs-spy="scroll" id="scroll-nav">
    """
    find_replace("C:/Users/Admin/Documents/GitHub/opensourcegisdata/v3-v2-merge/state", old, new)
    find_replace("C:/Users/Admin/Documents/GitHub/opensourcegisdata/v3-v2-merge/us-federal", old, new)


def fnr3():
    old2 = """
    Open Source GIS Data
    """
    new2 = """
    Open Source GIS Data Results
    """
    find_replace("C:/Users/Admin/Documents/GitHub/opensourcegisdata/v3-v2-merge/state", old2, new2)
    find_replace("C:/Users/Admin/Documents/GitHub/opensourcegisdata/v3-v2-merge/us-federal", old2, new2)
    
def replace_state_menus():
    old_state_menu = """
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <div class="container">
                <a class="navbar-brand" href="../index.html">Open Source GIS Data</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                        <li class="nav-item"><a class="nav-link" href="../index.html">Home</a></li>
                        <li class="nav-item"><a class="nav-link" href="../about.html">About</a></li>
                        <li class="nav-item"><a class="nav-link" href="../contact.html">Contact</a></li>
                    </ul>
                </div>
            </div>
        </nav>
    """
    new_state_menu = """
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <div class="container">
                <a class="navbar-brand" href="../index.html">Open Source GIS Data</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                        <li class="nav-item"><a class="nav-link" href="../index.html">Home</a></li>
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                              Categories
                            </a>
                            <ul class="dropdown-menu">
                                <li><a class="dropdown-item" href="../state/index.html">US Sources</a></li>
                                <li><a class="dropdown-item" href="../us-federal/index.html">US Federal Sources</a></li>
                                <li><a class="dropdown-item" href="../international/index.html">International</a></li>
                                <li><a class="dropdown-item" href="../software/index.html">Software</a></li>
                                <li><a class="dropdown-item" href="../resources/index.html">Resources</a></li>
                                <li><a class="dropdown-item" href="../tutorials/index.html">Tutorials</a></li>
                            </ul>
                        </li>
                        <li class="nav-item"><a class="nav-link" href="../about.html">About</a></li>
                        <li class="nav-item"><a class="nav-link" href="../contact.html">Contact</a></li>
                    </ul>
                </div>
            </div>
        </nav>
    """

    find_replace("C:/Users/Admin/Documents/GitHub/opensourcegisdata/v1/state", old_state_menu, new_state_menu)
    find_replace("C:/Users/Admin/Documents/GitHub/opensourcegisdata/v1/us-federal", old_state_menu, new_state_menu)

def link_update():
    find_replace("C:/Users/Admin/Documents/GitHub/opensourcegisdata/v1", '="http', '="https')
    find_replace("C:/Users/Admin/Documents/GitHub/opensourcegisdata/v1", '="httpss', '="https')

def st_geo_json_update():
    find_replace_json("C:/Users/Admin/Documents/GitHub/opensourcegisdata/v1", 'FIELD3', 'ST_GEO_PORTAL_URL')