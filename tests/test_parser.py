import sys
sys.path.append("..")
from parse_invoice.parser import *
from parse_invoice.configuration import *
import test_data as t
import unittest


class ParserTestCase(unittest.TestCase):
    """ Tests for py """

    '''parse_invoice_numbers tests'''
    def test_parse_invoice_numbers_input_1_sanity(self):
        invoice_numbers = parse_invoice_numbers(t.input_user_story_1)
        self.assertEquals(invoice_numbers, t.output_user_story_1)

    def test_parse_invoice_numbers_input_2_sanity(self):
        invoice_numbers = parse_invoice_numbers(t.input_user_story_2)
        self.assertEquals(invoice_numbers, t.output_user_story_2)

    def test_parse_invoice_numbers_regular(self):
        invoice_number = parse_invoice_numbers(t.test_input_regular_one_line)
        self.assertEquals(invoice_number, t.test_output_regular_one_line)
        invoice_numbers = parse_invoice_numbers(t.test_input_regular_two_lines)
        self.assertEquals(invoice_numbers, t.test_output_regular_two_lines)

    def test_parse_invoice_numbers_8_digits(self):
        self.assertRaises(ValueError, parse_invoice_numbers, t.test_input_8_digits)

    def test_parse_invoice_numbers_shoter_line(self):
        self.assertRaises(ValueError, parse_invoice_numbers, t.test_input_shorter_line)

    def test_parse_invoice_numbers_longer_line(self):
        self.assertRaises(ValueError, parse_invoice_numbers, t.test_input_longer_line)

    def test_parse_invoice_numbers_invalid_segment_size(self):
        self.assertRaises(ValueError, parse_invoice_numbers, t.test_input_invalid_segment_size)

    '''convert_chars_line_to_boolean_vector tests'''
    def test_convert_chars_line_to_boolean_vector_regular(self):
        self.assertEquals(len(t.test_chars_line), chars_in_line)

    def test_convert_chars_line_to_boolean_vector_short_line(self):
        self.assertRaises(ValueError, convert_chars_line_to_boolean_vector, t.test_chars_line_short)

    def test_convert_chars_line_to_boolean_vector_long_line(self):
        self.assertRaises(ValueError, convert_chars_line_to_boolean_vector, t.test_chars_line_long)

if __name__ == '__main__':
    unittest.main()
