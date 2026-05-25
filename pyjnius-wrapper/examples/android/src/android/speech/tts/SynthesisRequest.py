from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SynthesisRequest"]

class SynthesisRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/speech/tts/SynthesisRequest"
    __javaconstructor__ = [("(Ljava/lang/String;Landroid/os/Bundle;)V", False), ("(Ljava/lang/CharSequence;Landroid/os/Bundle;)V", False)]
    getText = JavaMethod("()Ljava/lang/String;")
    getCharSequenceText = JavaMethod("()Ljava/lang/CharSequence;")
    getVoiceName = JavaMethod("()Ljava/lang/String;")
    getLanguage = JavaMethod("()Ljava/lang/String;")
    getCountry = JavaMethod("()Ljava/lang/String;")
    getVariant = JavaMethod("()Ljava/lang/String;")
    getSpeechRate = JavaMethod("()I")
    getPitch = JavaMethod("()I")
    getParams = JavaMethod("()Landroid/os/Bundle;")
    getCallerUid = JavaMethod("()I")