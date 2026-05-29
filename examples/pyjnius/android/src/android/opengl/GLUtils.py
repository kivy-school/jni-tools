from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GLUtils"]

class GLUtils(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/opengl/GLUtils"
    getInternalFormat = JavaStaticMethod("(Landroid/graphics/Bitmap;)I")
    texSubImage2D = JavaMultipleMethod([("(IIIILandroid/graphics/Bitmap;)V", True, False), ("(IIIILandroid/graphics/Bitmap;II)V", True, False)])
    getEGLErrorString = JavaStaticMethod("(I)Ljava/lang/String;")
    texImage2D = JavaMultipleMethod([("(IIILandroid/graphics/Bitmap;I)V", True, False), ("(IIILandroid/graphics/Bitmap;II)V", True, False), ("(IILandroid/graphics/Bitmap;I)V", True, False)])
    getType = JavaStaticMethod("(Landroid/graphics/Bitmap;)I")