from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Deflater"]

class Deflater(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/zip/Deflater"
    __javaconstructor__ = [("(IZ)V", False), ("(I)V", False), ("()V", False)]
    BEST_COMPRESSION = JavaStaticField("I")
    BEST_SPEED = JavaStaticField("I")
    DEFAULT_COMPRESSION = JavaStaticField("I")
    DEFAULT_STRATEGY = JavaStaticField("I")
    DEFLATED = JavaStaticField("I")
    FILTERED = JavaStaticField("I")
    FULL_FLUSH = JavaStaticField("I")
    HUFFMAN_ONLY = JavaStaticField("I")
    NO_COMPRESSION = JavaStaticField("I")
    NO_FLUSH = JavaStaticField("I")
    SYNC_FLUSH = JavaStaticField("I")
    setInput = JavaMultipleMethod([("([BII)V", False, False), ("([B)V", False, False), ("(Ljava/nio/ByteBuffer;)V", False, False)])
    setDictionary = JavaMultipleMethod([("([BII)V", False, False), ("([B)V", False, False), ("(Ljava/nio/ByteBuffer;)V", False, False)])
    setStrategy = JavaMethod("(I)V")
    setLevel = JavaMethod("(I)V")
    needsInput = JavaMethod("()Z")
    finish = JavaMethod("()V")
    finished = JavaMethod("()Z")
    deflate = JavaMultipleMethod([("([BII)I", False, False), ("([B)I", False, False), ("(Ljava/nio/ByteBuffer;)I", False, False), ("([BIII)I", False, False), ("(Ljava/nio/ByteBuffer;I)I", False, False)])
    getAdler = JavaMethod("()I")
    getTotalIn = JavaMethod("()I")
    getBytesRead = JavaMethod("()J")
    getTotalOut = JavaMethod("()I")
    getBytesWritten = JavaMethod("()J")
    reset = JavaMethod("()V")
    end = JavaMethod("()V")