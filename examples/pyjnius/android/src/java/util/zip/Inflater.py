from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Inflater"]

class Inflater(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/zip/Inflater"
    __javaconstructor__ = [("(Z)V", False), ("()V", False)]
    setInput = JavaMultipleMethod([("([BII)V", False, False), ("([B)V", False, False), ("(Ljava/nio/ByteBuffer;)V", False, False)])
    setDictionary = JavaMultipleMethod([("([BII)V", False, False), ("([B)V", False, False), ("(Ljava/nio/ByteBuffer;)V", False, False)])
    getRemaining = JavaMethod("()I")
    needsInput = JavaMethod("()Z")
    needsDictionary = JavaMethod("()Z")
    finished = JavaMethod("()Z")
    inflate = JavaMultipleMethod([("([BII)I", False, False), ("([B)I", False, False), ("(Ljava/nio/ByteBuffer;)I", False, False)])
    getAdler = JavaMethod("()I")
    getTotalIn = JavaMethod("()I")
    getBytesRead = JavaMethod("()J")
    getTotalOut = JavaMethod("()I")
    getBytesWritten = JavaMethod("()J")
    reset = JavaMethod("()V")
    end = JavaMethod("()V")