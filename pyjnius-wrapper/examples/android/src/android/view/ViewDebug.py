from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ViewDebug"]

class ViewDebug(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/ViewDebug"
    __javaconstructor__ = [("()V", False)]
    TRACE_HIERARCHY = JavaStaticField("Z")
    TRACE_RECYCLER = JavaStaticField("Z")
    trace = JavaMultipleMethod([("(Landroid/view/View;Landroid/view/ViewDebug$RecyclerTraceType;[I)V", True, True), ("(Landroid/view/View;Landroid/view/ViewDebug$HierarchyTraceType;)V", True, False)])
    startRecyclerTracing = JavaStaticMethod("(Ljava/lang/String;Landroid/view/View;)V")
    stopRecyclerTracing = JavaStaticMethod("()V")
    startHierarchyTracing = JavaStaticMethod("(Ljava/lang/String;Landroid/view/View;)V")
    stopHierarchyTracing = JavaStaticMethod("()V")
    dumpCapturedView = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/Object;)V")

    class CapturedViewProperty(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ViewDebug/CapturedViewProperty"
        retrieveReturn = JavaMethod("()Z")

    class ExportedProperty(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ViewDebug/ExportedProperty"
        resolveId = JavaMethod("()Z")
        mapping = JavaMethod("()[Landroid/view/ViewDebug$IntToString;")
        indexMapping = JavaMethod("()[Landroid/view/ViewDebug$IntToString;")
        flagMapping = JavaMethod("()[Landroid/view/ViewDebug$FlagToString;")
        deepExport = JavaMethod("()Z")
        prefix = JavaMethod("()Ljava/lang/String;")
        category = JavaMethod("()Ljava/lang/String;")
        formatToHexString = JavaMethod("()Z")
        hasAdjacentMapping = JavaMethod("()Z")

    class FlagToString(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ViewDebug/FlagToString"
        mask = JavaMethod("()I")
        equals = JavaMethod("()I")
        name = JavaMethod("()Ljava/lang/String;")
        outputIf = JavaMethod("()Z")

    class HierarchyTraceType(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ViewDebug/HierarchyTraceType"
        values = JavaStaticMethod("()[Landroid/view/ViewDebug$HierarchyTraceType;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/view/ViewDebug$HierarchyTraceType;")
        INVALIDATE = JavaStaticField("Landroid/view/ViewDebug/HierarchyTraceType;")
        INVALIDATE_CHILD = JavaStaticField("Landroid/view/ViewDebug/HierarchyTraceType;")
        INVALIDATE_CHILD_IN_PARENT = JavaStaticField("Landroid/view/ViewDebug/HierarchyTraceType;")
        REQUEST_LAYOUT = JavaStaticField("Landroid/view/ViewDebug/HierarchyTraceType;")
        ON_LAYOUT = JavaStaticField("Landroid/view/ViewDebug/HierarchyTraceType;")
        ON_MEASURE = JavaStaticField("Landroid/view/ViewDebug/HierarchyTraceType;")
        DRAW = JavaStaticField("Landroid/view/ViewDebug/HierarchyTraceType;")
        BUILD_CACHE = JavaStaticField("Landroid/view/ViewDebug/HierarchyTraceType;")

    class IntToString(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ViewDebug/IntToString"
        from = JavaMethod("()I")
        to = JavaMethod("()Ljava/lang/String;")

    class RecyclerTraceType(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ViewDebug/RecyclerTraceType"
        values = JavaStaticMethod("()[Landroid/view/ViewDebug$RecyclerTraceType;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/view/ViewDebug$RecyclerTraceType;")
        NEW_VIEW = JavaStaticField("Landroid/view/ViewDebug/RecyclerTraceType;")
        BIND_VIEW = JavaStaticField("Landroid/view/ViewDebug/RecyclerTraceType;")
        RECYCLE_FROM_ACTIVE_HEAP = JavaStaticField("Landroid/view/ViewDebug/RecyclerTraceType;")
        RECYCLE_FROM_SCRAP_HEAP = JavaStaticField("Landroid/view/ViewDebug/RecyclerTraceType;")
        MOVE_TO_SCRAP_HEAP = JavaStaticField("Landroid/view/ViewDebug/RecyclerTraceType;")
        MOVE_FROM_ACTIVE_TO_SCRAP_HEAP = JavaStaticField("Landroid/view/ViewDebug/RecyclerTraceType;")