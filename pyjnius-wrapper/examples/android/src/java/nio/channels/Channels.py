from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Channels"]

class Channels(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/Channels"
    newInputStream = JavaMultipleMethod([("(Ljava/nio/channels/ReadableByteChannel;)Ljava/io/InputStream;", True, False), ("(Ljava/nio/channels/AsynchronousByteChannel;)Ljava/io/InputStream;", True, False)])
    newOutputStream = JavaMultipleMethod([("(Ljava/nio/channels/WritableByteChannel;)Ljava/io/OutputStream;", True, False), ("(Ljava/nio/channels/AsynchronousByteChannel;)Ljava/io/OutputStream;", True, False)])
    newChannel = JavaMultipleMethod([("(Ljava/io/InputStream;)Ljava/nio/channels/ReadableByteChannel;", True, False), ("(Ljava/io/OutputStream;)Ljava/nio/channels/WritableByteChannel;", True, False)])
    newReader = JavaMultipleMethod([("(Ljava/nio/channels/ReadableByteChannel;Ljava/nio/charset/CharsetDecoder;I)Ljava/io/Reader;", True, False), ("(Ljava/nio/channels/ReadableByteChannel;Ljava/lang/String;)Ljava/io/Reader;", True, False), ("(Ljava/nio/channels/ReadableByteChannel;Ljava/nio/charset/Charset;)Ljava/io/Reader;", True, False)])
    newWriter = JavaMultipleMethod([("(Ljava/nio/channels/WritableByteChannel;Ljava/nio/charset/CharsetEncoder;I)Ljava/io/Writer;", True, False), ("(Ljava/nio/channels/WritableByteChannel;Ljava/lang/String;)Ljava/io/Writer;", True, False), ("(Ljava/nio/channels/WritableByteChannel;Ljava/nio/charset/Charset;)Ljava/io/Writer;", True, False)])