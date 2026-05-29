from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Translator"]

class Translator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/translation/Translator"
    isDestroyed = JavaMethod("()Z")
    destroy = JavaMethod("()V")
    translate = JavaMethod("(Landroid/view/translation/TranslationRequest;Landroid/os/CancellationSignal;Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")