from utils.paser import arg_parse


if __name__ == '__main__':
    # return args from command line
    agr = arg_parse()
    if agr.g:
        # GUI on
        pass
    else:
        # GUI off
        pass
