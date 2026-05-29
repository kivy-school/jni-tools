from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Inflater"]

class Inflater(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/zip/Inflater"
    __javaconstructor__ = [("(Z)V", False), ("()V", False)]
    reset = JavaMethod("()V")
    inflate = JavaMultipleMethod([("([BII)I", False, False), ("([B)I", False, False), ("(Ljava/nio/ByteBuffer;)I", False, False)])
    end = JavaMethod("()V")
    close = JavaMethod("()V")
    setInput = JavaMultipleMethod([("([B)V", False, False), ("([BII)V", False, False), ("(Ljava/nio/ByteBuffer;)V", False, False)])
    getBytesWritten = JavaMethod("()J")
    finished = JavaMethod("()Z")
    needsDictionary = JavaMethod("()Z")
    needsInput = JavaMethod("()Z")
    setDictionary = JavaMultipleMethod([("([BII)V", False, False), ("(Ljava/nio/ByteBuffer;)V", False, False), ("([B)V", False, False)])
    getAdler = JavaMethod("()I")
    getBytesRead = JavaMethod("()J")
    getRemaining = JavaMethod("()I")
    getTotalIn = JavaMethod("()I")
    getTotalOut = JavaMethod("()I")