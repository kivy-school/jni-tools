from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ViewDebug"]

class ViewDebug(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/ViewDebug"
    __javaconstructor__ = [("()V", False)]
    TRACE_HIERARCHY = JavaStaticField("Z")
    TRACE_RECYCLER = JavaStaticField("Z")
    dumpCapturedView = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/Object;)V")
    startHierarchyTracing = JavaStaticMethod("(Ljava/lang/String;Landroid/view/View;)V")
    startRecyclerTracing = JavaStaticMethod("(Ljava/lang/String;Landroid/view/View;)V")
    stopHierarchyTracing = JavaStaticMethod("()V")
    stopRecyclerTracing = JavaStaticMethod("()V")
    trace = JavaMultipleMethod([("(Landroid/view/View;Landroid/view/ViewDebug$HierarchyTraceType;)V", True, False), ("(Landroid/view/View;Landroid/view/ViewDebug$RecyclerTraceType;[I)V", True, True)])

    class RecyclerTraceType(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ViewDebug$RecyclerTraceType"
        BIND_VIEW = JavaStaticField("Landroid/view/ViewDebug$RecyclerTraceType;")
        MOVE_FROM_ACTIVE_TO_SCRAP_HEAP = JavaStaticField("Landroid/view/ViewDebug$RecyclerTraceType;")
        MOVE_TO_SCRAP_HEAP = JavaStaticField("Landroid/view/ViewDebug$RecyclerTraceType;")
        NEW_VIEW = JavaStaticField("Landroid/view/ViewDebug$RecyclerTraceType;")
        RECYCLE_FROM_ACTIVE_HEAP = JavaStaticField("Landroid/view/ViewDebug$RecyclerTraceType;")
        RECYCLE_FROM_SCRAP_HEAP = JavaStaticField("Landroid/view/ViewDebug$RecyclerTraceType;")
        values = JavaStaticMethod("()[Landroid/view/ViewDebug$RecyclerTraceType;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/view/ViewDebug$RecyclerTraceType;")
        BIND_VIEW = JavaStaticField("Landroid/view/ViewDebug$RecyclerTraceType;")
        MOVE_FROM_ACTIVE_TO_SCRAP_HEAP = JavaStaticField("Landroid/view/ViewDebug$RecyclerTraceType;")
        MOVE_TO_SCRAP_HEAP = JavaStaticField("Landroid/view/ViewDebug$RecyclerTraceType;")
        NEW_VIEW = JavaStaticField("Landroid/view/ViewDebug$RecyclerTraceType;")
        RECYCLE_FROM_ACTIVE_HEAP = JavaStaticField("Landroid/view/ViewDebug$RecyclerTraceType;")
        RECYCLE_FROM_SCRAP_HEAP = JavaStaticField("Landroid/view/ViewDebug$RecyclerTraceType;")

    class IntToString(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ViewDebug$IntToString"
        from = JavaMethod("()I")
        to = JavaMethod("()Ljava/lang/String;")

    class HierarchyTraceType(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ViewDebug$HierarchyTraceType"
        BUILD_CACHE = JavaStaticField("Landroid/view/ViewDebug$HierarchyTraceType;")
        DRAW = JavaStaticField("Landroid/view/ViewDebug$HierarchyTraceType;")
        INVALIDATE = JavaStaticField("Landroid/view/ViewDebug$HierarchyTraceType;")
        INVALIDATE_CHILD = JavaStaticField("Landroid/view/ViewDebug$HierarchyTraceType;")
        INVALIDATE_CHILD_IN_PARENT = JavaStaticField("Landroid/view/ViewDebug$HierarchyTraceType;")
        ON_LAYOUT = JavaStaticField("Landroid/view/ViewDebug$HierarchyTraceType;")
        ON_MEASURE = JavaStaticField("Landroid/view/ViewDebug$HierarchyTraceType;")
        REQUEST_LAYOUT = JavaStaticField("Landroid/view/ViewDebug$HierarchyTraceType;")
        values = JavaStaticMethod("()[Landroid/view/ViewDebug$HierarchyTraceType;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/view/ViewDebug$HierarchyTraceType;")
        BUILD_CACHE = JavaStaticField("Landroid/view/ViewDebug$HierarchyTraceType;")
        DRAW = JavaStaticField("Landroid/view/ViewDebug$HierarchyTraceType;")
        INVALIDATE = JavaStaticField("Landroid/view/ViewDebug$HierarchyTraceType;")
        INVALIDATE_CHILD = JavaStaticField("Landroid/view/ViewDebug$HierarchyTraceType;")
        INVALIDATE_CHILD_IN_PARENT = JavaStaticField("Landroid/view/ViewDebug$HierarchyTraceType;")
        ON_LAYOUT = JavaStaticField("Landroid/view/ViewDebug$HierarchyTraceType;")
        ON_MEASURE = JavaStaticField("Landroid/view/ViewDebug$HierarchyTraceType;")
        REQUEST_LAYOUT = JavaStaticField("Landroid/view/ViewDebug$HierarchyTraceType;")

    class FlagToString(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ViewDebug$FlagToString"
        name = JavaMethod("()Ljava/lang/String;")
        equals = JavaMethod("()I")
        mask = JavaMethod("()I")
        outputIf = JavaMethod("()Z")

    class ExportedProperty(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ViewDebug$ExportedProperty"
        formatToHexString = JavaMethod("()Z")
        prefix = JavaMethod("()Ljava/lang/String;")
        mapping = JavaMethod("()[Landroid/view/ViewDebug$IntToString;")
        flagMapping = JavaMethod("()[Landroid/view/ViewDebug$FlagToString;")
        deepExport = JavaMethod("()Z")
        category = JavaMethod("()Ljava/lang/String;")
        hasAdjacentMapping = JavaMethod("()Z")
        indexMapping = JavaMethod("()[Landroid/view/ViewDebug$IntToString;")
        resolveId = JavaMethod("()Z")

    class CapturedViewProperty(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ViewDebug$CapturedViewProperty"
        retrieveReturn = JavaMethod("()Z")