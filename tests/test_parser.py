from pysgf import SGF, Move
import os


def test_simple():
    input_sgf = "(;GM[1]FF[4]SZ[19]DT[2020-04-12]AB[dd][dj];B[dp];W[pp];B[pj])"
    root = SGF.parse(input_sgf)
    assert "4" == root["FF"]
    assert root["XYZ"] is None
    assert "dp" == root.children[0]["B"]
    assert input_sgf == str(root)


def test_branch():
    input_sgf = "(;GM[1]FF[4]CA[UTF-8]AP[Sabaki:0.43.3]KM[6.5]SZ[19]DT[2020-04-12]AB[dd][dj](;B[dp];W[pp](;B[pj])(;PL[B]AW[jp]C[sdfdsfdsf]))(;B[pd]))"
    root = SGF.parse(input_sgf)
    assert input_sgf == str(root)


def test_weird_escape():
    input_sgf = """(;GM[1]FF[4]CA[UTF-8]AP[Sabaki:0.43.3]KM[6.5]SZ[19]DT[2020-04-12]C[how does it escape
[
or \\]
])"""
    root = SGF.parse(input_sgf)
    assert input_sgf == str(root)


def test_alphago():
    file = os.path.join(os.path.dirname(__file__), "data/LS vs AG - G4 - English.sgf")
    tree = SGF.parse_file(file)


def test_pandanet():
    file = os.path.join(os.path.dirname(__file__), "data/panda1.sgf")
    root = SGF.parse_file(file)
    root_props = {
        "GM",
        "EV",
        "US",
        "CoPyright",
        "GN",
        "RE",
        "PW",
        "WR",
        "NW",
        "PB",
        "BR",
        "NB",
        "PC",
        "DT",
        "SZ",
        "TM",
        "KM",
        "LT",
        "RR",
        "HA",
        "AB",
        "C",
    }
    assert root_props == root.properties.keys()

    move = root
    while move.children:
        move = move.children[0]
    assert 94 == len(move["TW"])
    assert "Trilan" == move["OS"]


def test_ogs():
    file = os.path.join(os.path.dirname(__file__), "data/ogs.sgf")
    tree = SGF.parse_file(file)
