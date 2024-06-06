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

def replace():
    
    findold = '''
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

    
        '''
    replacenew = '''
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <div class="container">
                <a class="navbar-brand" href="https://opensourcegisdata.com">Open Source GIS Data</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                        <li class="nav-item"><a class="nav-link" href="https://opensourcegisdata.com">Home</a></li>
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                              Categories
                            </a>
                            <ul class="dropdown-menu">
                                <li><a class="dropdown-item" href="../state/index.html">US Sources</a></li>
                                <li><a class="dropdown-item" href="../us-federal/index.html">US Federal Sources</a></li>
                            </ul>
                        </li>
                        <li class="nav-item"><a class="nav-link" href="https://galileo.gisdata.io">Search</a></li>
                    </ul>
                </div>
            </div>
        </nav>       
        '''
    #find_replace("C:/Users/Admin/Documents/GitHub/opensourcegisdata/v1/state", findold, replacenew)
    find_replace("C:/Users/Admin/Documents/GitHub/opensourcegisdata/v1/us-federal", findold, replacenew)