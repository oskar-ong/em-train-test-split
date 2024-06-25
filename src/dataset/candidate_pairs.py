def write_ditto_file(blocked):
    train = []

    for index, row in blocked.iterrows():
        current_row = ''
        
        cid_l = ''
        cid_r = ''
        
        for col_name, value in row.items():
            if (col_name == 'CID_l'):
                cid_l = value
                continue
            
            if (col_name == 'CID_r'):
                cid_r = value
                continue

            current_row += 'COL '
            current_row += col_name 
            current_row += ' VAL '
            current_row += str(value)

            if (col_name == 'artist_l'):
                current_row += '\t'
            else:
                current_row += ' '

        current_row += '\t '
        if (cid_l == cid_r):
            current_row += str(1)
        else:
            current_row += str(0)

            
        train.append(current_row)

    with open('./data/interim/blocked-labeled.txt', 'w') as file:
        for item in train:
            file.write(f"{item}\n")

    return True
