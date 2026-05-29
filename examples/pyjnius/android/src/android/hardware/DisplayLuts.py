from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DisplayLuts"]

class DisplayLuts(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/DisplayLuts"
    __javaconstructor__ = [("()V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    set = JavaMultipleMethod([("(Landroid/hardware/DisplayLuts$Entry;)V", False, False), ("(Landroid/hardware/DisplayLuts$Entry;Landroid/hardware/DisplayLuts$Entry;)V", False, False)])

    class Entry(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/DisplayLuts$Entry"
        __javaconstructor__ = [("([FII)V", False)]
        getSamplingKey = JavaMethod("()I")
        getBuffer = JavaMethod("()[F")
        toString = JavaMethod("()Ljava/lang/String;")
        getDimension = JavaMethod("()I")