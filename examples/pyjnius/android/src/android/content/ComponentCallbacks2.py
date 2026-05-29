from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ComponentCallbacks2"]

class ComponentCallbacks2(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/ComponentCallbacks2"
    TRIM_MEMORY_BACKGROUND = JavaStaticField("I")
    TRIM_MEMORY_COMPLETE = JavaStaticField("I")
    TRIM_MEMORY_MODERATE = JavaStaticField("I")
    TRIM_MEMORY_RUNNING_CRITICAL = JavaStaticField("I")
    TRIM_MEMORY_RUNNING_LOW = JavaStaticField("I")
    TRIM_MEMORY_RUNNING_MODERATE = JavaStaticField("I")
    TRIM_MEMORY_UI_HIDDEN = JavaStaticField("I")
    onTrimMemory = JavaMethod("(I)V")