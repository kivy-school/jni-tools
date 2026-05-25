from typing import Any, ClassVar, overload
from java.io.InputStream import InputStream
from java.io.OutputStream import OutputStream
from java.io.Reader import Reader
from java.io.Writer import Writer
from java.nio.channels.AsynchronousByteChannel import AsynchronousByteChannel
from java.nio.channels.ReadableByteChannel import ReadableByteChannel
from java.nio.channels.WritableByteChannel import WritableByteChannel
from java.nio.charset.Charset import Charset
from java.nio.charset.CharsetDecoder import CharsetDecoder
from java.nio.charset.CharsetEncoder import CharsetEncoder

class Channels:
    @overload
    @staticmethod
    def newInputStream(arg0: ReadableByteChannel) -> InputStream: ...
    @overload
    @staticmethod
    def newInputStream(arg0: AsynchronousByteChannel) -> InputStream: ...
    @overload
    @staticmethod
    def newOutputStream(arg0: WritableByteChannel) -> OutputStream: ...
    @overload
    @staticmethod
    def newOutputStream(arg0: AsynchronousByteChannel) -> OutputStream: ...
    @overload
    @staticmethod
    def newChannel(arg0: InputStream) -> ReadableByteChannel: ...
    @overload
    @staticmethod
    def newChannel(arg0: OutputStream) -> WritableByteChannel: ...
    @overload
    @staticmethod
    def newReader(arg0: ReadableByteChannel, arg1: CharsetDecoder, arg2: int) -> Reader: ...
    @overload
    @staticmethod
    def newReader(arg0: ReadableByteChannel, arg1: str) -> Reader: ...
    @overload
    @staticmethod
    def newReader(arg0: ReadableByteChannel, arg1: Charset) -> Reader: ...
    @overload
    @staticmethod
    def newWriter(arg0: WritableByteChannel, arg1: CharsetEncoder, arg2: int) -> Writer: ...
    @overload
    @staticmethod
    def newWriter(arg0: WritableByteChannel, arg1: str) -> Writer: ...
    @overload
    @staticmethod
    def newWriter(arg0: WritableByteChannel, arg1: Charset) -> Writer: ...
