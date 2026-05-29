from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LiveFolders"]

class LiveFolders(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/provider/LiveFolders"
    ACTION_CREATE_LIVE_FOLDER = JavaStaticField("Ljava/lang/String;")
    DESCRIPTION = JavaStaticField("Ljava/lang/String;")
    DISPLAY_MODE_GRID = JavaStaticField("I")
    DISPLAY_MODE_LIST = JavaStaticField("I")
    EXTRA_LIVE_FOLDER_BASE_INTENT = JavaStaticField("Ljava/lang/String;")
    EXTRA_LIVE_FOLDER_DISPLAY_MODE = JavaStaticField("Ljava/lang/String;")
    EXTRA_LIVE_FOLDER_ICON = JavaStaticField("Ljava/lang/String;")
    EXTRA_LIVE_FOLDER_NAME = JavaStaticField("Ljava/lang/String;")
    ICON_BITMAP = JavaStaticField("Ljava/lang/String;")
    ICON_PACKAGE = JavaStaticField("Ljava/lang/String;")
    ICON_RESOURCE = JavaStaticField("Ljava/lang/String;")
    INTENT = JavaStaticField("Ljava/lang/String;")
    NAME = JavaStaticField("Ljava/lang/String;")
    _COUNT = JavaStaticField("Ljava/lang/String;")
    _ID = JavaStaticField("Ljava/lang/String;")