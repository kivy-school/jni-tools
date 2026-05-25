from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Translator"]

class Translator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/translation/Translator"
    translate = JavaMethod("(Landroid/view/translation/TranslationRequest;Landroid/os/CancellationSignal;Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    destroy = JavaMethod("()V")
    isDestroyed = JavaMethod("()Z")