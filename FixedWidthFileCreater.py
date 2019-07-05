from collections import OrderedDict, namedtuple


class FixedWidthFileCreater:
    """
    This class contains all methods required to make a Fixed Width File.
    """

    def __init__(self):
        """
        Initialize:
        1. file name,
        2. encoding
        3. data types
        """
        self.start_pos = 0
        self.file_name = input('Enter the name of the File to be created: ')
        self.encoding_type = input('File encoding(utf-8/utf-16/ascii): ').lower()
        self.file = open(self.file_name, 'a', encoding=self.encoding_type)
        self.positions = namedtuple('positions', ['from_pos', 'to_pos'])
        self.data = ''
        self.fields_mappings = ''
        self.rows = list()

    def get_field_names(self):
        """
        Input:
        1. Field name (The name should start with an alphabet)
        2. from position (The start position of the field, should start from "1")
        3. to position (The end position of the field)
        """
        self.fields_mappings = OrderedDict()
        print('Enter "BREAK" to stop code')
        last_pos = 0
        field_pos = 1
        length_of_field = 0
        while 1:
            field_name = input('Enter the name of field: \n')
            if field_name.upper() == 'BREAK':
                break
            from_pos = int(input('From pos: \n'))
            to_pos = int(input('To position: \n'))
            pos = self.positions(from_pos=from_pos, to_pos=to_pos)
            self.fields_mappings[field_name] = pos
        self.data = namedtuple('data', list(self.fields_mappings.keys()))

    def get_field_values(self):
        """
        Input:
        1. No of rows to be written in the file.
        2. Values of the field-names that were given earlier.
        """
        for x in range(int(input('Enter the no of rows to enter into file:\n'))):
            data_row = dict()
            for field in self.data._fields:
                field_val = input('Enter the value of {}: \n'.format(field))
                data_row[field] = field_val
            # '**data_row' converts the 'data_row' dictionary into named-tuple 'data'
            data_row = self.data(**data_row)
            self.rows.append(data_row)
            # print(self.fields_mappings)
            print(self.rows)

    def create_write_template(self, data):
        """
        :param data: This will contain all the values of current row in a namedTuple, i.e.,
            1. field value,
            2. from position,
            3. to position
        :return: Will return the final row to be written in the file/csv, with all the correct spaces
        """
        self.fields_mappings = OrderedDict(sorted(self.fields_mappings.items(), key=lambda e: e[1].from_pos))
        no_of_keys = len(self.fields_mappings.keys())
        keys_list = list(self.fields_mappings.keys())
        final = ''
        for idx in range(no_of_keys-1):
            curr_from_pos = self.fields_mappings.get(keys_list[idx]).from_pos

            curr_to_pos = self.fields_mappings.get(keys_list[idx]).to_pos
            # if the first field does not start with 1, then need to add spaces before
            if curr_from_pos != 1 and idx == 0:
                final = final + (' ' * (curr_from_pos - 1))
            # get the total space b/w the current and the next field
            length_between_fields = self.fields_mappings.get(keys_list[idx+1]).from_pos - curr_from_pos
            # get the length of the value of the field,
            # check whether it is in or out of the indexes of the field length
            avail_length_of_val = curr_to_pos - curr_from_pos + 1
            length_of_val = len(str(getattr(data, keys_list[idx])).strip())

            # if not then add the extra spaces at the end of the field
            if length_of_val <= avail_length_of_val:
                final = final + str(getattr(data, keys_list[idx]))
                final = final + (' ' * (length_between_fields - length_of_val))
            # if it is out of index, limit the field value in bounds
            else:
                final = final + str(getattr(data, keys_list[idx]))[:curr_to_pos-curr_from_pos+1]
            # Check if the last field is properly inserted.
            print(
                f'FieldName: {keys_list[idx]}\n'
                f'cFrom: {curr_from_pos}\n'
                f'cTo: {curr_to_pos}\n'
                f'Len bw Fields: {length_between_fields}\n'
                f'Avail length of field{avail_length_of_val}\n'
                f'Len of val: {length_of_val}\n\n'
            )

        curr_from_pos = self.fields_mappings.get(keys_list[-1]).from_pos
        curr_to_pos = self.fields_mappings.get(keys_list[-1]).to_pos
        if curr_from_pos != 1 and no_of_keys == 1:
            final = final + (' ' * (curr_from_pos - 1))
        avail_length_of_val = curr_to_pos - curr_from_pos + 1
        length_of_val = len(str(getattr(data, keys_list[-1])).strip())
        if length_of_val <= avail_length_of_val:
            print('Here')
            final = final + str(getattr(data, keys_list[-1]))
            final = final + (' ' * (avail_length_of_val - length_of_val))
        else:
            final = final + str(getattr(data, keys_list[-1]))[:curr_to_pos - curr_from_pos + 1]
        print(f'FieldName: {keys_list[-1]}\ncFrom: {curr_from_pos}\ncTo: {curr_to_pos}\nAvailable Len of Fields: {avail_length_of_val}\nLen of val: {length_of_val}\n\n')
        print('>>>>>', final)
        return final

    def write_to_file(self, writable_row):
        """
        :param writable_row: this contains a string that is the final row to be written into the file.
        :return: N/A
        """
        print(writable_row, file=self.file)

    def main(self):
        self.get_field_names()
        self.get_field_values()
        for data in self.rows:
            writable_row = self.create_write_template(data)
            self.write_to_file(writable_row)

        print('Done With The code!!!!')


if __name__ == '__main__':
    file_creater = FixedWidthFileCreater()
    file_creater.main()

