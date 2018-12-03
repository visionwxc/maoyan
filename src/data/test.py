from Program import program

if __name__ == '__main__':
    wxc = program('wxc', 24, 80)
    print(dir(wxc))
    print(wxc.__dict__)
    print(wxc.__str__())