from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SynthesisCallback"]

class SynthesisCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/speech/tts/SynthesisCallback"
    done = JavaMethod("()I")
    start = JavaMethod("(III)I")
    rangeStart = JavaMethod("(III)V")
    getMaxBufferSize = JavaMethod("()I")
    hasStarted = JavaMethod("()Z")
    hasFinished = JavaMethod("()Z")
    audioAvailable = JavaMethod("([BII)I")
    error = JavaMultipleMethod([("()V", False, False), ("(I)V", False, False)])