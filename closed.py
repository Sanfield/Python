def funx():
    x=[5]
    def funy():
        x[0] *= x[0]
        return x[0]
    return funy()
