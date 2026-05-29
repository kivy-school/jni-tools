from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Deflater"]

class Deflater(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/zip/Deflater"
    __javaconstructor__ = [("()V", False), ("(I)V", False), ("(IZ)V", False)]
    DEFLATED = JavaStaticField("I")
    NO_COMPRESSION = JavaStaticField("I")
    BEST_SPEED = JavaStaticField("I")
    BEST_COMPRESSION = JavaStaticField("I")
    DEFAULT_COMPRESSION = JavaStaticField("I")
    FILTERED = JavaStaticField("I")
    HUFFMAN_ONLY = JavaStaticField("I")
    DEFAULT_STRATEGY = JavaStaticField("I")
    NO_FLUSH = JavaStaticField("I")
    SYNC_FLUSH = JavaStaticField("I")
    FULL_FLUSH = JavaStaticField("I")
    reset = JavaMethod("()V")
    end = JavaMethod("()V")
    close = JavaMethod("()V")
    finish = JavaMethod("()V")
    deflate = JavaMultipleMethod([("([B)I", False, False), ("(Ljava/nio/ByteBuffer;)I", False, False), ("([BIII)I", False, False), ("([BII)I", False, False), ("(Ljava/nio/ByteBuffer;I)I", False, False)])
    setLevel = JavaMethod("(I)V")
    setInput = JavaMultipleMethod([("([BII)V", False, False), ("([B)V", False, False), ("(Ljava/nio/ByteBuffer;)V", False, False)])
    getBytesWritten = JavaMethod("()J")
    finished = JavaMethod("()Z")
    needsInput = JavaMethod("()Z")
    setDictionary = JavaMultipleMethod([("([BII)V", False, False), ("([B)V", False, False), ("(Ljava/nio/ByteBuffer;)V", False, False)])
    getAdler = JavaMethod("()I")
    getBytesRead = JavaMethod("()J")
    getTotalIn = JavaMethod("()I")
    getTotalOut = JavaMethod("()I")
    setStrategy = JavaMethod("(I)V")