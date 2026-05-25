from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnifiedNativeAdAssetNames"]

class UnifiedNativeAdAssetNames(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/formats/UnifiedNativeAdAssetNames"
    __javaconstructor__ = [("()V", False)]
    ASSET_HEADLINE = JavaStaticField("Ljava/lang/String;")
    ASSET_CALL_TO_ACTION = JavaStaticField("Ljava/lang/String;")
    ASSET_ICON = JavaStaticField("Ljava/lang/String;")
    ASSET_BODY = JavaStaticField("Ljava/lang/String;")
    ASSET_ADVERTISER = JavaStaticField("Ljava/lang/String;")
    ASSET_STORE = JavaStaticField("Ljava/lang/String;")
    ASSET_PRICE = JavaStaticField("Ljava/lang/String;")
    ASSET_IMAGE = JavaStaticField("Ljava/lang/String;")
    ASSET_STAR_RATING = JavaStaticField("Ljava/lang/String;")
    ASSET_MEDIA_VIDEO = JavaStaticField("Ljava/lang/String;")
    ASSET_ADCHOICES_CONTAINER_VIEW = JavaStaticField("Ljava/lang/String;")