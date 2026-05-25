from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ImageSpan"]

class ImageSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/ImageSpan"
    __javaconstructor__ = [("(Landroid/graphics/Bitmap;)V", False), ("(Landroid/graphics/Bitmap;I)V", False), ("(Landroid/content/Context;Landroid/graphics/Bitmap;)V", False), ("(Landroid/content/Context;Landroid/graphics/Bitmap;I)V", False), ("(Landroid/graphics/drawable/Drawable;)V", False), ("(Landroid/graphics/drawable/Drawable;I)V", False), ("(Landroid/graphics/drawable/Drawable;Ljava/lang/String;)V", False), ("(Landroid/graphics/drawable/Drawable;Ljava/lang/String;I)V", False), ("(Landroid/content/Context;Landroid/net/Uri;)V", False), ("(Landroid/content/Context;Landroid/net/Uri;I)V", False), ("(Landroid/content/Context;I)V", False), ("(Landroid/content/Context;II)V", False)]
    getDrawable = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    getSource = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")