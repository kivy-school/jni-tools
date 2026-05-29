from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SynthesisCallback"]

class SynthesisCallback(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/speech/tts/SynthesisCallback"
    getMaxBufferSize = JavaMethod("()I")
    start = JavaMethod("(III)I")
    audioAvailable = JavaMethod("([BII)I")
    done = JavaMethod("()I")
    error = JavaMultipleMethod([("()V", False, False), ("(I)V", False, False)])
    hasStarted = JavaMethod("()Z")
    hasFinished = JavaMethod("()Z")
    rangeStart = JavaMethod("(III)V")