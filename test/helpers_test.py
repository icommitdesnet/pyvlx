"""Unit tests helpers module."""
import unittest

from pyvlx.exception import PyVLXException
from pyvlx.helpers import bytes_to_string, string_to_bytes, bytes_from_statusflags, statusflags_from_bytes


class TestString(unittest.TestCase):
    """Test class for String encoding/decoding."""

    # pylint: disable=too-many-public-methods,invalid-name

    def test_encoding(self):
        """Test simple encoding."""
        self.assertEqual(string_to_bytes("fnord", 10), b"fnord" + bytes(5))

    def test_encoding_without_padding(self):
        """Test encoding with exact match of size."""
        self.assertEqual(string_to_bytes("fnord", 5), b"fnord")

    def test_encoding_failure(self):
        """Test error while encoding."""
        with self.assertRaises(PyVLXException):
            string_to_bytes("fnord", 4)

    def test_decoding(self):
        """Test decoding of string."""
        self.assertEqual(bytes_to_string(b"fnord" + bytes(5)), "fnord")

    def test_decoding_without_padding(self):
        """Test decoding of string without padding."""
        self.assertEqual(bytes_to_string(b"fnord"), "fnord")

    def test_encode_utf8(self):
        """Test encoding a string with special characters."""
        self.assertEqual(
            string_to_bytes("Fenster Büro", 16), b"Fenster B\xc3\xbcro\x00\x00\x00"
        )

    def test_decode_utf8(self):
        """Test decoding a string with special characters."""
        self.assertEqual(
            bytes_to_string(b"Fenster B\xc3\xbcro\x00\x00\x00"), "Fenster Büro"
        )

    def test_statusflags_from_bytes(self):
        """Test decoding statusflags to list."""
        self.assertEqual(
            statusflags_from_bytes(0x0211.to_bytes(2, byteorder="big")), [1, 8, 12]
        )

    def bytes_from_statusflags(self):
        """Test decoding statusflags to list."""
        self.assertEqual(
            bytes_from_statusflags([1, 8, 12], 2), 0x0211.to_bytes(2, byteorder="big")
        )