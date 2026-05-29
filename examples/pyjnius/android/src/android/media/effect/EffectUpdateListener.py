from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EffectUpdateListener"]

class EffectUpdateListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/effect/EffectUpdateListener"
    onEffectUpdated = JavaMethod("(Landroid/media/effect/Effect;Ljava/lang/Object;)V")