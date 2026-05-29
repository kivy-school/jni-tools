from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RenderEffect"]

class RenderEffect(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/RenderEffect"
    createBitmapEffect = JavaMultipleMethod([("(Landroid/graphics/Bitmap;Landroid/graphics/Rect;Landroid/graphics/Rect;)Landroid/graphics/RenderEffect;", True, False), ("(Landroid/graphics/Bitmap;)Landroid/graphics/RenderEffect;", True, False)])
    createBlendModeEffect = JavaStaticMethod("(Landroid/graphics/RenderEffect;Landroid/graphics/RenderEffect;Landroid/graphics/BlendMode;)Landroid/graphics/RenderEffect;")
    createBlurEffect = JavaMultipleMethod([("(FFLandroid/graphics/RenderEffect;Landroid/graphics/Shader$TileMode;)Landroid/graphics/RenderEffect;", True, False), ("(FFLandroid/graphics/Shader$TileMode;)Landroid/graphics/RenderEffect;", True, False)])
    createChainEffect = JavaStaticMethod("(Landroid/graphics/RenderEffect;Landroid/graphics/RenderEffect;)Landroid/graphics/RenderEffect;")
    createColorFilterEffect = JavaMultipleMethod([("(Landroid/graphics/ColorFilter;Landroid/graphics/RenderEffect;)Landroid/graphics/RenderEffect;", True, False), ("(Landroid/graphics/ColorFilter;)Landroid/graphics/RenderEffect;", True, False)])
    createOffsetEffect = JavaMultipleMethod([("(FF)Landroid/graphics/RenderEffect;", True, False), ("(FFLandroid/graphics/RenderEffect;)Landroid/graphics/RenderEffect;", True, False)])
    createRuntimeShaderEffect = JavaStaticMethod("(Landroid/graphics/RuntimeShader;Ljava/lang/String;)Landroid/graphics/RenderEffect;")
    createShaderEffect = JavaStaticMethod("(Landroid/graphics/Shader;)Landroid/graphics/RenderEffect;")