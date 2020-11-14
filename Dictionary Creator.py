inputf = open('elem.txt', 'r')
outputf = open('output.txt', 'w')
for i in inputf:
    i = i.strip()
    words = i.split()
    for ii in words:
        try:
            ii = int(ii)
            outputf.write(str(ii) + ':' + ' ')
        except ValueError:
            if len(ii) < 3:
                # it was a string, not an int.
                outputf.write('\'' + str(ii) + '\'' + ',' + '\n')
    # if ii.isdigit:
    #     outputf.write(str(ii) + ',' + '\n')
    # elif ii.isalpha:
    #     if len(ii) < 3:
    #         outputf.write(str(ii) + ':' + ' ')
