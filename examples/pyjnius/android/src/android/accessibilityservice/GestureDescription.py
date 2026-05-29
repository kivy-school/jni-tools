from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GestureDescription"]

class GestureDescription(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/accessibilityservice/GestureDescription"
    getStrokeCount = JavaMethod("()I")
    getMaxStrokeCount = JavaStaticMethod("()I")
    getStroke = JavaMethod("(I)Landroid/accessibilityservice/GestureDescription$StrokeDescription;")
    getMaxGestureDuration = JavaStaticMethod("()J")
    getDisplayId = JavaMethod("()I")

    class StrokeDescription(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/accessibilityservice/GestureDescription$StrokeDescription"
        __javaconstructor__ = [("(Landroid/graphics/Path;JJ)V", False), ("(Landroid/graphics/Path;JJZ)V", False)]
        willContinue = JavaMethod("()Z")
        continueStroke = JavaMethod("(Landroid/graphics/Path;JJZ)Landroid/accessibilityservice/GestureDescription$StrokeDescription;")
        getPath = JavaMethod("()Landroid/graphics/Path;")
        getStartTime = JavaMethod("()J")
        getDuration = JavaMethod("()J")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/accessibilityservice/GestureDescription$Builder"
        __javaconstructor__ = [("()V", False)]
        addStroke = JavaMethod("(Landroid/accessibilityservice/GestureDescription$StrokeDescription;)Landroid/accessibilityservice/GestureDescription$Builder;")
        setDisplayId = JavaMethod("(I)Landroid/accessibilityservice/GestureDescription$Builder;")
        build = JavaMethod("()Landroid/accessibilityservice/GestureDescription;")