from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LevelListDrawable"]

class LevelListDrawable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/LevelListDrawable"
    __javaconstructor__ = [("()V", False)]
    addLevel = JavaMethod("(IILandroid/graphics/drawable/Drawable;)V")
    inflate = JavaMethod("(Landroid/content/res/Resources;Lorg/xmlpull/v1/XmlPullParser;Landroid/util/AttributeSet;Landroid/content/res/Resources$Theme;)V")
    mutate = JavaMethod("()Landroid/graphics/drawable/Drawable;")