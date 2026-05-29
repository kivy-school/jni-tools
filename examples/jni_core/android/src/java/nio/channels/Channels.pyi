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
    def newWriter(p0: WritableByteChannel, p1: CharsetEncoder, p2: int) -> Writer: ...
    @overload
    @staticmethod
    def newWriter(p0: WritableByteChannel, p1: str) -> Writer: ...
    @overload
    @staticmethod
    def newWriter(p0: WritableByteChannel, p1: Charset) -> Writer: ...
    @overload
    @staticmethod
    def newChannel(p0: OutputStream) -> WritableByteChannel: ...
    @overload
    @staticmethod
    def newChannel(p0: InputStream) -> ReadableByteChannel: ...
    @overload
    @staticmethod
    def newInputStream(p0: ReadableByteChannel) -> InputStream: ...
    @overload
    @staticmethod
    def newInputStream(p0: AsynchronousByteChannel) -> InputStream: ...
    @overload
    @staticmethod
    def newOutputStream(p0: WritableByteChannel) -> OutputStream: ...
    @overload
    @staticmethod
    def newOutputStream(p0: AsynchronousByteChannel) -> OutputStream: ...
    @overload
    @staticmethod
    def newReader(p0: ReadableByteChannel, p1: str) -> Reader: ...
    @overload
    @staticmethod
    def newReader(p0: ReadableByteChannel, p1: CharsetDecoder, p2: int) -> Reader: ...
    @overload
    @staticmethod
    def newReader(p0: ReadableByteChannel, p1: Charset) -> Reader: ...
