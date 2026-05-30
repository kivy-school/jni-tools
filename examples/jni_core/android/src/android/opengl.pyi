from typing import Any, ClassVar, overload
from android.hardware.SyncFence import SyncFence
from android.opengl.EGLDisplay import EGLDisplay
from android.opengl.EGLSurface import EGLSurface
from android.opengl.EGLSync import EGLSync

class EGLExt:
    EGL_CONTEXT_FLAGS_KHR: ClassVar[int]
    EGL_CONTEXT_MAJOR_VERSION_KHR: ClassVar[int]
    EGL_CONTEXT_MINOR_VERSION_KHR: ClassVar[int]
    EGL_NO_NATIVE_FENCE_FD_ANDROID: ClassVar[int]
    EGL_OPENGL_ES3_BIT_KHR: ClassVar[int]
    EGL_RECORDABLE_ANDROID: ClassVar[int]
    EGL_SYNC_NATIVE_FENCE_ANDROID: ClassVar[int]
    EGL_SYNC_NATIVE_FENCE_FD_ANDROID: ClassVar[int]
    EGL_SYNC_NATIVE_FENCE_SIGNALED_ANDROID: ClassVar[int]
    def __init__(self) -> None: ...
    @staticmethod
    def eglDupNativeFenceFDANDROID(p0: EGLDisplay, p1: EGLSync) -> SyncFence: ...
    @staticmethod
    def eglPresentationTimeANDROID(p0: EGLDisplay, p1: EGLSurface, p2: int) -> bool: ...

from typing import Any, ClassVar, overload
from java.nio.ByteBuffer import ByteBuffer
from java.nio.IntBuffer import IntBuffer

class GLES31Ext:
    GL_BLEND_ADVANCED_COHERENT_KHR: ClassVar[int]
    GL_BUFFER_KHR: ClassVar[int]
    GL_CLAMP_TO_BORDER_EXT: ClassVar[int]
    GL_COLORBURN_KHR: ClassVar[int]
    GL_COLORDODGE_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_10x10_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_10x5_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_10x6_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_10x8_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_12x10_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_12x12_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_4x4_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_5x4_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_5x5_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_6x5_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_6x6_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_8x5_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_8x6_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_8x8_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x10_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x5_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x6_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x8_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_12x10_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_12x12_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_4x4_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_5x4_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_5x5_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_6x5_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_6x6_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x5_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x6_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x8_KHR: ClassVar[int]
    GL_CONTEXT_FLAG_DEBUG_BIT_KHR: ClassVar[int]
    GL_DARKEN_KHR: ClassVar[int]
    GL_DEBUG_CALLBACK_FUNCTION_KHR: ClassVar[int]
    GL_DEBUG_CALLBACK_USER_PARAM_KHR: ClassVar[int]
    GL_DEBUG_GROUP_STACK_DEPTH_KHR: ClassVar[int]
    GL_DEBUG_LOGGED_MESSAGES_KHR: ClassVar[int]
    GL_DEBUG_NEXT_LOGGED_MESSAGE_LENGTH_KHR: ClassVar[int]
    GL_DEBUG_OUTPUT_KHR: ClassVar[int]
    GL_DEBUG_OUTPUT_SYNCHRONOUS_KHR: ClassVar[int]
    GL_DEBUG_SEVERITY_HIGH_KHR: ClassVar[int]
    GL_DEBUG_SEVERITY_LOW_KHR: ClassVar[int]
    GL_DEBUG_SEVERITY_MEDIUM_KHR: ClassVar[int]
    GL_DEBUG_SEVERITY_NOTIFICATION_KHR: ClassVar[int]
    GL_DEBUG_SOURCE_API_KHR: ClassVar[int]
    GL_DEBUG_SOURCE_APPLICATION_KHR: ClassVar[int]
    GL_DEBUG_SOURCE_OTHER_KHR: ClassVar[int]
    GL_DEBUG_SOURCE_SHADER_COMPILER_KHR: ClassVar[int]
    GL_DEBUG_SOURCE_THIRD_PARTY_KHR: ClassVar[int]
    GL_DEBUG_SOURCE_WINDOW_SYSTEM_KHR: ClassVar[int]
    GL_DEBUG_TYPE_DEPRECATED_BEHAVIOR_KHR: ClassVar[int]
    GL_DEBUG_TYPE_ERROR_KHR: ClassVar[int]
    GL_DEBUG_TYPE_MARKER_KHR: ClassVar[int]
    GL_DEBUG_TYPE_OTHER_KHR: ClassVar[int]
    GL_DEBUG_TYPE_PERFORMANCE_KHR: ClassVar[int]
    GL_DEBUG_TYPE_POP_GROUP_KHR: ClassVar[int]
    GL_DEBUG_TYPE_PORTABILITY_KHR: ClassVar[int]
    GL_DEBUG_TYPE_PUSH_GROUP_KHR: ClassVar[int]
    GL_DEBUG_TYPE_UNDEFINED_BEHAVIOR_KHR: ClassVar[int]
    GL_DECODE_EXT: ClassVar[int]
    GL_DIFFERENCE_KHR: ClassVar[int]
    GL_EXCLUSION_KHR: ClassVar[int]
    GL_FIRST_VERTEX_CONVENTION_EXT: ClassVar[int]
    GL_FRACTIONAL_EVEN_EXT: ClassVar[int]
    GL_FRACTIONAL_ODD_EXT: ClassVar[int]
    GL_FRAGMENT_INTERPOLATION_OFFSET_BITS_OES: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_LAYERED_EXT: ClassVar[int]
    GL_FRAMEBUFFER_DEFAULT_LAYERS_EXT: ClassVar[int]
    GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS_EXT: ClassVar[int]
    GL_GEOMETRY_LINKED_INPUT_TYPE_EXT: ClassVar[int]
    GL_GEOMETRY_LINKED_OUTPUT_TYPE_EXT: ClassVar[int]
    GL_GEOMETRY_LINKED_VERTICES_OUT_EXT: ClassVar[int]
    GL_GEOMETRY_SHADER_BIT_EXT: ClassVar[int]
    GL_GEOMETRY_SHADER_EXT: ClassVar[int]
    GL_GEOMETRY_SHADER_INVOCATIONS_EXT: ClassVar[int]
    GL_HARDLIGHT_KHR: ClassVar[int]
    GL_HSL_COLOR_KHR: ClassVar[int]
    GL_HSL_HUE_KHR: ClassVar[int]
    GL_HSL_LUMINOSITY_KHR: ClassVar[int]
    GL_HSL_SATURATION_KHR: ClassVar[int]
    GL_IMAGE_BUFFER_EXT: ClassVar[int]
    GL_IMAGE_CUBE_MAP_ARRAY_EXT: ClassVar[int]
    GL_INT_IMAGE_BUFFER_EXT: ClassVar[int]
    GL_INT_IMAGE_CUBE_MAP_ARRAY_EXT: ClassVar[int]
    GL_INT_SAMPLER_2D_MULTISAMPLE_ARRAY_OES: ClassVar[int]
    GL_INT_SAMPLER_BUFFER_EXT: ClassVar[int]
    GL_INT_SAMPLER_CUBE_MAP_ARRAY_EXT: ClassVar[int]
    GL_ISOLINES_EXT: ClassVar[int]
    GL_IS_PER_PATCH_EXT: ClassVar[int]
    GL_LAST_VERTEX_CONVENTION_EXT: ClassVar[int]
    GL_LAYER_PROVOKING_VERTEX_EXT: ClassVar[int]
    GL_LIGHTEN_KHR: ClassVar[int]
    GL_LINES_ADJACENCY_EXT: ClassVar[int]
    GL_LINE_STRIP_ADJACENCY_EXT: ClassVar[int]
    GL_MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_COMBINED_TESS_CONTROL_UNIFORM_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_COMBINED_TESS_EVALUATION_UNIFORM_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_DEBUG_GROUP_STACK_DEPTH_KHR: ClassVar[int]
    GL_MAX_DEBUG_LOGGED_MESSAGES_KHR: ClassVar[int]
    GL_MAX_DEBUG_MESSAGE_LENGTH_KHR: ClassVar[int]
    GL_MAX_FRAGMENT_INTERPOLATION_OFFSET_OES: ClassVar[int]
    GL_MAX_FRAMEBUFFER_LAYERS_EXT: ClassVar[int]
    GL_MAX_GEOMETRY_ATOMIC_COUNTERS_EXT: ClassVar[int]
    GL_MAX_GEOMETRY_ATOMIC_COUNTER_BUFFERS_EXT: ClassVar[int]
    GL_MAX_GEOMETRY_IMAGE_UNIFORMS_EXT: ClassVar[int]
    GL_MAX_GEOMETRY_INPUT_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_GEOMETRY_OUTPUT_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_GEOMETRY_OUTPUT_VERTICES_EXT: ClassVar[int]
    GL_MAX_GEOMETRY_SHADER_INVOCATIONS_EXT: ClassVar[int]
    GL_MAX_GEOMETRY_SHADER_STORAGE_BLOCKS_EXT: ClassVar[int]
    GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS_EXT: ClassVar[int]
    GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_GEOMETRY_UNIFORM_BLOCKS_EXT: ClassVar[int]
    GL_MAX_GEOMETRY_UNIFORM_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_LABEL_LENGTH_KHR: ClassVar[int]
    GL_MAX_PATCH_VERTICES_EXT: ClassVar[int]
    GL_MAX_TESS_CONTROL_ATOMIC_COUNTERS_EXT: ClassVar[int]
    GL_MAX_TESS_CONTROL_ATOMIC_COUNTER_BUFFERS_EXT: ClassVar[int]
    GL_MAX_TESS_CONTROL_IMAGE_UNIFORMS_EXT: ClassVar[int]
    GL_MAX_TESS_CONTROL_INPUT_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_TESS_CONTROL_OUTPUT_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_TESS_CONTROL_SHADER_STORAGE_BLOCKS_EXT: ClassVar[int]
    GL_MAX_TESS_CONTROL_TEXTURE_IMAGE_UNITS_EXT: ClassVar[int]
    GL_MAX_TESS_CONTROL_TOTAL_OUTPUT_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_TESS_CONTROL_UNIFORM_BLOCKS_EXT: ClassVar[int]
    GL_MAX_TESS_CONTROL_UNIFORM_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_TESS_EVALUATION_ATOMIC_COUNTERS_EXT: ClassVar[int]
    GL_MAX_TESS_EVALUATION_ATOMIC_COUNTER_BUFFERS_EXT: ClassVar[int]
    GL_MAX_TESS_EVALUATION_IMAGE_UNIFORMS_EXT: ClassVar[int]
    GL_MAX_TESS_EVALUATION_INPUT_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_TESS_EVALUATION_OUTPUT_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_TESS_EVALUATION_SHADER_STORAGE_BLOCKS_EXT: ClassVar[int]
    GL_MAX_TESS_EVALUATION_TEXTURE_IMAGE_UNITS_EXT: ClassVar[int]
    GL_MAX_TESS_EVALUATION_UNIFORM_BLOCKS_EXT: ClassVar[int]
    GL_MAX_TESS_EVALUATION_UNIFORM_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_TESS_GEN_LEVEL_EXT: ClassVar[int]
    GL_MAX_TESS_PATCH_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_TEXTURE_BUFFER_SIZE_EXT: ClassVar[int]
    GL_MIN_FRAGMENT_INTERPOLATION_OFFSET_OES: ClassVar[int]
    GL_MIN_SAMPLE_SHADING_VALUE_OES: ClassVar[int]
    GL_MULTIPLY_KHR: ClassVar[int]
    GL_OVERLAY_KHR: ClassVar[int]
    GL_PATCHES_EXT: ClassVar[int]
    GL_PATCH_VERTICES_EXT: ClassVar[int]
    GL_PRIMITIVES_GENERATED_EXT: ClassVar[int]
    GL_PRIMITIVE_BOUNDING_BOX_EXT: ClassVar[int]
    GL_PRIMITIVE_RESTART_FOR_PATCHES_SUPPORTED: ClassVar[int]
    GL_PROGRAM_KHR: ClassVar[int]
    GL_QUADS_EXT: ClassVar[int]
    GL_QUERY_KHR: ClassVar[int]
    GL_REFERENCED_BY_GEOMETRY_SHADER_EXT: ClassVar[int]
    GL_REFERENCED_BY_TESS_CONTROL_SHADER_EXT: ClassVar[int]
    GL_REFERENCED_BY_TESS_EVALUATION_SHADER_EXT: ClassVar[int]
    GL_SAMPLER_2D_MULTISAMPLE_ARRAY_OES: ClassVar[int]
    GL_SAMPLER_BUFFER_EXT: ClassVar[int]
    GL_SAMPLER_CUBE_MAP_ARRAY_EXT: ClassVar[int]
    GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW_EXT: ClassVar[int]
    GL_SAMPLER_KHR: ClassVar[int]
    GL_SAMPLE_SHADING_OES: ClassVar[int]
    GL_SCREEN_KHR: ClassVar[int]
    GL_SHADER_KHR: ClassVar[int]
    GL_SKIP_DECODE_EXT: ClassVar[int]
    GL_SOFTLIGHT_KHR: ClassVar[int]
    GL_STACK_OVERFLOW_KHR: ClassVar[int]
    GL_STACK_UNDERFLOW_KHR: ClassVar[int]
    GL_STENCIL_INDEX8_OES: ClassVar[int]
    GL_STENCIL_INDEX_OES: ClassVar[int]
    GL_TESS_CONTROL_OUTPUT_VERTICES_EXT: ClassVar[int]
    GL_TESS_CONTROL_SHADER_BIT_EXT: ClassVar[int]
    GL_TESS_CONTROL_SHADER_EXT: ClassVar[int]
    GL_TESS_EVALUATION_SHADER_BIT_EXT: ClassVar[int]
    GL_TESS_EVALUATION_SHADER_EXT: ClassVar[int]
    GL_TESS_GEN_MODE_EXT: ClassVar[int]
    GL_TESS_GEN_POINT_MODE_EXT: ClassVar[int]
    GL_TESS_GEN_SPACING_EXT: ClassVar[int]
    GL_TESS_GEN_VERTEX_ORDER_EXT: ClassVar[int]
    GL_TEXTURE_2D_MULTISAMPLE_ARRAY_OES: ClassVar[int]
    GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY_OES: ClassVar[int]
    GL_TEXTURE_BINDING_BUFFER_EXT: ClassVar[int]
    GL_TEXTURE_BINDING_CUBE_MAP_ARRAY_EXT: ClassVar[int]
    GL_TEXTURE_BORDER_COLOR_EXT: ClassVar[int]
    GL_TEXTURE_BUFFER_BINDING_EXT: ClassVar[int]
    GL_TEXTURE_BUFFER_DATA_STORE_BINDING_EXT: ClassVar[int]
    GL_TEXTURE_BUFFER_EXT: ClassVar[int]
    GL_TEXTURE_BUFFER_OFFSET_ALIGNMENT_EXT: ClassVar[int]
    GL_TEXTURE_BUFFER_OFFSET_EXT: ClassVar[int]
    GL_TEXTURE_BUFFER_SIZE_EXT: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_ARRAY_EXT: ClassVar[int]
    GL_TEXTURE_SRGB_DECODE_EXT: ClassVar[int]
    GL_TRIANGLES_ADJACENCY_EXT: ClassVar[int]
    GL_TRIANGLE_STRIP_ADJACENCY_EXT: ClassVar[int]
    GL_UNDEFINED_VERTEX_EXT: ClassVar[int]
    GL_UNSIGNED_INT_IMAGE_BUFFER_EXT: ClassVar[int]
    GL_UNSIGNED_INT_IMAGE_CUBE_MAP_ARRAY_EXT: ClassVar[int]
    GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE_ARRAY_OES: ClassVar[int]
    GL_UNSIGNED_INT_SAMPLER_BUFFER_EXT: ClassVar[int]
    GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY_EXT: ClassVar[int]
    GL_VERTEX_ARRAY_KHR: ClassVar[int]
    @staticmethod
    def glBlendBarrierKHR() -> None: ...
    @staticmethod
    def glBlendEquationSeparateiEXT(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glBlendEquationiEXT(p0: int, p1: int) -> None: ...
    @staticmethod
    def glBlendFuncSeparateiEXT(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @staticmethod
    def glBlendFunciEXT(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glColorMaskiEXT(p0: int, p1: bool, p2: bool, p3: bool, p4: bool) -> None: ...
    @staticmethod
    def glCopyImageSubDataEXT(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: int, p9: int, p10: int, p11: int, p12: int, p13: int, p14: int) -> None: ...
    @staticmethod
    def glDebugMessageCallbackKHR(p0: Any) -> None: ...
    @overload
    @staticmethod
    def glDebugMessageControlKHR(p0: int, p1: int, p2: int, p3: int, p4: Any, p5: int, p6: bool) -> None: ...
    @overload
    @staticmethod
    def glDebugMessageControlKHR(p0: int, p1: int, p2: int, p3: int, p4: IntBuffer, p5: bool) -> None: ...
    @staticmethod
    def glDebugMessageInsertKHR(p0: int, p1: int, p2: int, p3: int, p4: str) -> None: ...
    @staticmethod
    def glDisableiEXT(p0: int, p1: int) -> None: ...
    @staticmethod
    def glEnableiEXT(p0: int, p1: int) -> None: ...
    @staticmethod
    def glFramebufferTextureEXT(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glGetDebugMessageCallbackKHR() -> Any: ...
    @overload
    @staticmethod
    def glGetDebugMessageLogKHR(p0: int, p1: IntBuffer, p2: IntBuffer, p3: IntBuffer, p4: IntBuffer) -> Any: ...
    @overload
    @staticmethod
    def glGetDebugMessageLogKHR(p0: int, p1: IntBuffer, p2: IntBuffer, p3: IntBuffer, p4: IntBuffer, p5: IntBuffer, p6: ByteBuffer) -> int: ...
    @overload
    @staticmethod
    def glGetDebugMessageLogKHR(p0: int, p1: int, p2: Any, p3: int, p4: Any, p5: int, p6: Any, p7: int, p8: Any, p9: int, p10: Any, p11: int, p12: Any, p13: int) -> int: ...
    @overload
    @staticmethod
    def glGetDebugMessageLogKHR(p0: int, p1: Any, p2: int, p3: Any, p4: int, p5: Any, p6: int, p7: Any, p8: int) -> Any: ...
    @staticmethod
    def glGetObjectLabelKHR(p0: int, p1: int) -> str: ...
    @staticmethod
    def glGetObjectPtrLabelKHR(p0: int) -> str: ...
    @overload
    @staticmethod
    def glGetSamplerParameterIivEXT(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetSamplerParameterIivEXT(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetSamplerParameterIuivEXT(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetSamplerParameterIuivEXT(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameterIivEXT(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameterIivEXT(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameterIuivEXT(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameterIuivEXT(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @staticmethod
    def glIsEnablediEXT(p0: int, p1: int) -> bool: ...
    @staticmethod
    def glMinSampleShadingOES(p0: float) -> None: ...
    @staticmethod
    def glObjectLabelKHR(p0: int, p1: int, p2: int, p3: str) -> None: ...
    @staticmethod
    def glObjectPtrLabelKHR(p0: int, p1: str) -> None: ...
    @staticmethod
    def glPatchParameteriEXT(p0: int, p1: int) -> None: ...
    @staticmethod
    def glPopDebugGroupKHR() -> None: ...
    @staticmethod
    def glPrimitiveBoundingBoxEXT(p0: float, p1: float, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float) -> None: ...
    @staticmethod
    def glPushDebugGroupKHR(p0: int, p1: int, p2: int, p3: str) -> None: ...
    @overload
    @staticmethod
    def glSamplerParameterIivEXT(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glSamplerParameterIivEXT(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glSamplerParameterIuivEXT(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glSamplerParameterIuivEXT(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def glTexBufferEXT(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glTexBufferRangeEXT(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @overload
    @staticmethod
    def glTexParameterIivEXT(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glTexParameterIivEXT(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glTexParameterIuivEXT(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glTexParameterIuivEXT(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @staticmethod
    def glTexStorage3DMultisampleOES(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: bool) -> None: ...

    class DebugProcKHR:
        def onMessage(self, p0: int, p1: int, p2: int, p3: int, p4: str) -> None: ...

from typing import Any, ClassVar, overload
from android.opengl.EGLConfig import EGLConfig
from android.opengl.EGLContext import EGLContext
from android.opengl.EGLDisplay import EGLDisplay
from android.opengl.EGLImage import EGLImage
from android.opengl.EGLSurface import EGLSurface
from android.opengl.EGLSync import EGLSync
from java.nio.Buffer import Buffer

class EGL15:
    EGL_CL_EVENT_HANDLE: ClassVar[int]
    EGL_CONDITION_SATISFIED: ClassVar[int]
    EGL_CONTEXT_MAJOR_VERSION: ClassVar[int]
    EGL_CONTEXT_MINOR_VERSION: ClassVar[int]
    EGL_CONTEXT_OPENGL_COMPATIBILITY_PROFILE_BIT: ClassVar[int]
    EGL_CONTEXT_OPENGL_CORE_PROFILE_BIT: ClassVar[int]
    EGL_CONTEXT_OPENGL_DEBUG: ClassVar[int]
    EGL_CONTEXT_OPENGL_FORWARD_COMPATIBLE: ClassVar[int]
    EGL_CONTEXT_OPENGL_PROFILE_MASK: ClassVar[int]
    EGL_CONTEXT_OPENGL_RESET_NOTIFICATION_STRATEGY: ClassVar[int]
    EGL_CONTEXT_OPENGL_ROBUST_ACCESS: ClassVar[int]
    EGL_FOREVER: ClassVar[int]
    EGL_GL_COLORSPACE: ClassVar[int]
    EGL_GL_COLORSPACE_LINEAR: ClassVar[int]
    EGL_GL_COLORSPACE_SRGB: ClassVar[int]
    EGL_GL_RENDERBUFFER: ClassVar[int]
    EGL_GL_TEXTURE_2D: ClassVar[int]
    EGL_GL_TEXTURE_3D: ClassVar[int]
    EGL_GL_TEXTURE_CUBE_MAP_NEGATIVE_X: ClassVar[int]
    EGL_GL_TEXTURE_CUBE_MAP_NEGATIVE_Y: ClassVar[int]
    EGL_GL_TEXTURE_CUBE_MAP_NEGATIVE_Z: ClassVar[int]
    EGL_GL_TEXTURE_CUBE_MAP_POSITIVE_X: ClassVar[int]
    EGL_GL_TEXTURE_CUBE_MAP_POSITIVE_Y: ClassVar[int]
    EGL_GL_TEXTURE_CUBE_MAP_POSITIVE_Z: ClassVar[int]
    EGL_GL_TEXTURE_LEVEL: ClassVar[int]
    EGL_GL_TEXTURE_ZOFFSET: ClassVar[int]
    EGL_IMAGE_PRESERVED: ClassVar[int]
    EGL_LOSE_CONTEXT_ON_RESET: ClassVar[int]
    EGL_NO_CONTEXT: ClassVar[EGLContext]
    EGL_NO_DISPLAY: ClassVar[EGLDisplay]
    EGL_NO_IMAGE: ClassVar[EGLImage]
    EGL_NO_RESET_NOTIFICATION: ClassVar[int]
    EGL_NO_SURFACE: ClassVar[EGLSurface]
    EGL_NO_SYNC: ClassVar[EGLSync]
    EGL_OPENGL_ES3_BIT: ClassVar[int]
    EGL_PLATFORM_ANDROID_KHR: ClassVar[int]
    EGL_SIGNALED: ClassVar[int]
    EGL_SYNC_CL_EVENT: ClassVar[int]
    EGL_SYNC_CL_EVENT_COMPLETE: ClassVar[int]
    EGL_SYNC_CONDITION: ClassVar[int]
    EGL_SYNC_FENCE: ClassVar[int]
    EGL_SYNC_FLUSH_COMMANDS_BIT: ClassVar[int]
    EGL_SYNC_PRIOR_COMMANDS_COMPLETE: ClassVar[int]
    EGL_SYNC_STATUS: ClassVar[int]
    EGL_SYNC_TYPE: ClassVar[int]
    EGL_TIMEOUT_EXPIRED: ClassVar[int]
    EGL_UNSIGNALED: ClassVar[int]
    @staticmethod
    def eglClientWaitSync(p0: EGLDisplay, p1: EGLSync, p2: int, p3: int) -> int: ...
    @staticmethod
    def eglCreateImage(p0: EGLDisplay, p1: EGLContext, p2: int, p3: int, p4: Any, p5: int) -> EGLImage: ...
    @staticmethod
    def eglCreatePlatformPixmapSurface(p0: EGLDisplay, p1: EGLConfig, p2: Buffer, p3: Any, p4: int) -> EGLSurface: ...
    @staticmethod
    def eglCreatePlatformWindowSurface(p0: EGLDisplay, p1: EGLConfig, p2: Buffer, p3: Any, p4: int) -> EGLSurface: ...
    @staticmethod
    def eglCreateSync(p0: EGLDisplay, p1: int, p2: Any, p3: int) -> EGLSync: ...
    @staticmethod
    def eglDestroyImage(p0: EGLDisplay, p1: EGLImage) -> bool: ...
    @staticmethod
    def eglDestroySync(p0: EGLDisplay, p1: EGLSync) -> bool: ...
    @staticmethod
    def eglGetPlatformDisplay(p0: int, p1: int, p2: Any, p3: int) -> EGLDisplay: ...
    @staticmethod
    def eglGetSyncAttrib(p0: EGLDisplay, p1: EGLSync, p2: int, p3: Any, p4: int) -> bool: ...
    @staticmethod
    def eglWaitSync(p0: EGLDisplay, p1: EGLSync, p2: int) -> bool: ...

from typing import Any, ClassVar, overload
from java.nio.Buffer import Buffer
from java.nio.FloatBuffer import FloatBuffer
from java.nio.IntBuffer import IntBuffer
from java.nio.ShortBuffer import ShortBuffer

class GLES11Ext:
    GL_3DC_XY_AMD: ClassVar[int]
    GL_3DC_X_AMD: ClassVar[int]
    GL_ATC_RGBA_EXPLICIT_ALPHA_AMD: ClassVar[int]
    GL_ATC_RGBA_INTERPOLATED_ALPHA_AMD: ClassVar[int]
    GL_ATC_RGB_AMD: ClassVar[int]
    GL_BGRA: ClassVar[int]
    GL_BLEND_DST_ALPHA_OES: ClassVar[int]
    GL_BLEND_DST_RGB_OES: ClassVar[int]
    GL_BLEND_EQUATION_ALPHA_OES: ClassVar[int]
    GL_BLEND_EQUATION_OES: ClassVar[int]
    GL_BLEND_EQUATION_RGB_OES: ClassVar[int]
    GL_BLEND_SRC_ALPHA_OES: ClassVar[int]
    GL_BLEND_SRC_RGB_OES: ClassVar[int]
    GL_BUFFER_ACCESS_OES: ClassVar[int]
    GL_BUFFER_MAPPED_OES: ClassVar[int]
    GL_BUFFER_MAP_POINTER_OES: ClassVar[int]
    GL_COLOR_ATTACHMENT0_OES: ClassVar[int]
    GL_CURRENT_PALETTE_MATRIX_OES: ClassVar[int]
    GL_DECR_WRAP_OES: ClassVar[int]
    GL_DEPTH24_STENCIL8_OES: ClassVar[int]
    GL_DEPTH_ATTACHMENT_OES: ClassVar[int]
    GL_DEPTH_COMPONENT16_OES: ClassVar[int]
    GL_DEPTH_COMPONENT24_OES: ClassVar[int]
    GL_DEPTH_COMPONENT32_OES: ClassVar[int]
    GL_DEPTH_STENCIL_OES: ClassVar[int]
    GL_ETC1_RGB8_OES: ClassVar[int]
    GL_FIXED_OES: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME_OES: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE_OES: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE_OES: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL_OES: ClassVar[int]
    GL_FRAMEBUFFER_BINDING_OES: ClassVar[int]
    GL_FRAMEBUFFER_COMPLETE_OES: ClassVar[int]
    GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT_OES: ClassVar[int]
    GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS_OES: ClassVar[int]
    GL_FRAMEBUFFER_INCOMPLETE_FORMATS_OES: ClassVar[int]
    GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT_OES: ClassVar[int]
    GL_FRAMEBUFFER_OES: ClassVar[int]
    GL_FRAMEBUFFER_UNSUPPORTED_OES: ClassVar[int]
    GL_FUNC_ADD_OES: ClassVar[int]
    GL_FUNC_REVERSE_SUBTRACT_OES: ClassVar[int]
    GL_FUNC_SUBTRACT_OES: ClassVar[int]
    GL_INCR_WRAP_OES: ClassVar[int]
    GL_INVALID_FRAMEBUFFER_OPERATION_OES: ClassVar[int]
    GL_MATRIX_INDEX_ARRAY_BUFFER_BINDING_OES: ClassVar[int]
    GL_MATRIX_INDEX_ARRAY_OES: ClassVar[int]
    GL_MATRIX_INDEX_ARRAY_POINTER_OES: ClassVar[int]
    GL_MATRIX_INDEX_ARRAY_SIZE_OES: ClassVar[int]
    GL_MATRIX_INDEX_ARRAY_STRIDE_OES: ClassVar[int]
    GL_MATRIX_INDEX_ARRAY_TYPE_OES: ClassVar[int]
    GL_MATRIX_PALETTE_OES: ClassVar[int]
    GL_MAX_CUBE_MAP_TEXTURE_SIZE_OES: ClassVar[int]
    GL_MAX_PALETTE_MATRICES_OES: ClassVar[int]
    GL_MAX_RENDERBUFFER_SIZE_OES: ClassVar[int]
    GL_MAX_TEXTURE_MAX_ANISOTROPY_EXT: ClassVar[int]
    GL_MAX_VERTEX_UNITS_OES: ClassVar[int]
    GL_MIRRORED_REPEAT_OES: ClassVar[int]
    GL_MODELVIEW_MATRIX_FLOAT_AS_INT_BITS_OES: ClassVar[int]
    GL_NONE_OES: ClassVar[int]
    GL_NORMAL_MAP_OES: ClassVar[int]
    GL_PROJECTION_MATRIX_FLOAT_AS_INT_BITS_OES: ClassVar[int]
    GL_REFLECTION_MAP_OES: ClassVar[int]
    GL_RENDERBUFFER_ALPHA_SIZE_OES: ClassVar[int]
    GL_RENDERBUFFER_BINDING_OES: ClassVar[int]
    GL_RENDERBUFFER_BLUE_SIZE_OES: ClassVar[int]
    GL_RENDERBUFFER_DEPTH_SIZE_OES: ClassVar[int]
    GL_RENDERBUFFER_GREEN_SIZE_OES: ClassVar[int]
    GL_RENDERBUFFER_HEIGHT_OES: ClassVar[int]
    GL_RENDERBUFFER_INTERNAL_FORMAT_OES: ClassVar[int]
    GL_RENDERBUFFER_OES: ClassVar[int]
    GL_RENDERBUFFER_RED_SIZE_OES: ClassVar[int]
    GL_RENDERBUFFER_STENCIL_SIZE_OES: ClassVar[int]
    GL_RENDERBUFFER_WIDTH_OES: ClassVar[int]
    GL_REQUIRED_TEXTURE_IMAGE_UNITS_OES: ClassVar[int]
    GL_RGB565_OES: ClassVar[int]
    GL_RGB5_A1_OES: ClassVar[int]
    GL_RGB8_OES: ClassVar[int]
    GL_RGBA4_OES: ClassVar[int]
    GL_RGBA8_OES: ClassVar[int]
    GL_SAMPLER_EXTERNAL_OES: ClassVar[int]
    GL_STENCIL_ATTACHMENT_OES: ClassVar[int]
    GL_STENCIL_INDEX1_OES: ClassVar[int]
    GL_STENCIL_INDEX4_OES: ClassVar[int]
    GL_STENCIL_INDEX8_OES: ClassVar[int]
    GL_TEXTURE_BINDING_CUBE_MAP_OES: ClassVar[int]
    GL_TEXTURE_BINDING_EXTERNAL_OES: ClassVar[int]
    GL_TEXTURE_CROP_RECT_OES: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_NEGATIVE_X_OES: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_NEGATIVE_Y_OES: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_NEGATIVE_Z_OES: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_OES: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_POSITIVE_X_OES: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_POSITIVE_Y_OES: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_POSITIVE_Z_OES: ClassVar[int]
    GL_TEXTURE_EXTERNAL_OES: ClassVar[int]
    GL_TEXTURE_GEN_MODE_OES: ClassVar[int]
    GL_TEXTURE_GEN_STR_OES: ClassVar[int]
    GL_TEXTURE_MATRIX_FLOAT_AS_INT_BITS_OES: ClassVar[int]
    GL_TEXTURE_MAX_ANISOTROPY_EXT: ClassVar[int]
    GL_UNSIGNED_INT_24_8_OES: ClassVar[int]
    GL_WEIGHT_ARRAY_BUFFER_BINDING_OES: ClassVar[int]
    GL_WEIGHT_ARRAY_OES: ClassVar[int]
    GL_WEIGHT_ARRAY_POINTER_OES: ClassVar[int]
    GL_WEIGHT_ARRAY_SIZE_OES: ClassVar[int]
    GL_WEIGHT_ARRAY_STRIDE_OES: ClassVar[int]
    GL_WEIGHT_ARRAY_TYPE_OES: ClassVar[int]
    GL_WRITE_ONLY_OES: ClassVar[int]
    def __init__(self) -> None: ...
    @staticmethod
    def glAlphaFuncxOES(p0: int, p1: int) -> None: ...
    @staticmethod
    def glBindFramebufferOES(p0: int, p1: int) -> None: ...
    @staticmethod
    def glBindRenderbufferOES(p0: int, p1: int) -> None: ...
    @staticmethod
    def glBlendEquationOES(p0: int) -> None: ...
    @staticmethod
    def glBlendEquationSeparateOES(p0: int, p1: int) -> None: ...
    @staticmethod
    def glBlendFuncSeparateOES(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glCheckFramebufferStatusOES(p0: int) -> int: ...
    @staticmethod
    def glClearColorxOES(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glClearDepthfOES(p0: float) -> None: ...
    @staticmethod
    def glClearDepthxOES(p0: int) -> None: ...
    @overload
    @staticmethod
    def glClipPlanefOES(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glClipPlanefOES(p0: int, p1: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glClipPlanexOES(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glClipPlanexOES(p0: int, p1: IntBuffer) -> None: ...
    @staticmethod
    def glColor4xOES(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glCurrentPaletteMatrixOES(p0: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteFramebuffersOES(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glDeleteFramebuffersOES(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteRenderbuffersOES(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteRenderbuffersOES(p0: int, p1: IntBuffer) -> None: ...
    @staticmethod
    def glDepthRangefOES(p0: float, p1: float) -> None: ...
    @staticmethod
    def glDepthRangexOES(p0: int, p1: int) -> None: ...
    @staticmethod
    def glDrawTexfOES(p0: float, p1: float, p2: float, p3: float, p4: float) -> None: ...
    @overload
    @staticmethod
    def glDrawTexfvOES(p0: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glDrawTexfvOES(p0: Any, p1: int) -> None: ...
    @staticmethod
    def glDrawTexiOES(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @overload
    @staticmethod
    def glDrawTexivOES(p0: Any, p1: int) -> None: ...
    @overload
    @staticmethod
    def glDrawTexivOES(p0: IntBuffer) -> None: ...
    @staticmethod
    def glDrawTexsOES(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @overload
    @staticmethod
    def glDrawTexsvOES(p0: Any, p1: int) -> None: ...
    @overload
    @staticmethod
    def glDrawTexsvOES(p0: ShortBuffer) -> None: ...
    @staticmethod
    def glDrawTexxOES(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @overload
    @staticmethod
    def glDrawTexxvOES(p0: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glDrawTexxvOES(p0: Any, p1: int) -> None: ...
    @staticmethod
    def glEGLImageTargetRenderbufferStorageOES(p0: int, p1: Buffer) -> None: ...
    @staticmethod
    def glEGLImageTargetTexture2DOES(p0: int, p1: Buffer) -> None: ...
    @staticmethod
    def glFogxOES(p0: int, p1: int) -> None: ...
    @overload
    @staticmethod
    def glFogxvOES(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glFogxvOES(p0: int, p1: IntBuffer) -> None: ...
    @staticmethod
    def glFramebufferRenderbufferOES(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glFramebufferTexture2DOES(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @staticmethod
    def glFrustumfOES(p0: float, p1: float, p2: float, p3: float, p4: float, p5: float) -> None: ...
    @staticmethod
    def glFrustumxOES(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int) -> None: ...
    @overload
    @staticmethod
    def glGenFramebuffersOES(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGenFramebuffersOES(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glGenRenderbuffersOES(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGenRenderbuffersOES(p0: int, p1: Any, p2: int) -> None: ...
    @staticmethod
    def glGenerateMipmapOES(p0: int) -> None: ...
    @overload
    @staticmethod
    def glGetClipPlanefOES(p0: int, p1: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetClipPlanefOES(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glGetClipPlanexOES(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetClipPlanexOES(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glGetFixedvOES(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glGetFixedvOES(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetFramebufferAttachmentParameterivOES(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glGetFramebufferAttachmentParameterivOES(p0: int, p1: int, p2: int, p3: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetLightxvOES(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetLightxvOES(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetMaterialxvOES(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetMaterialxvOES(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetRenderbufferParameterivOES(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetRenderbufferParameterivOES(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexEnvxvOES(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexEnvxvOES(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexGenfvOES(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexGenfvOES(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexGenivOES(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexGenivOES(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexGenxvOES(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexGenxvOES(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameterxvOES(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameterxvOES(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def glIsFramebufferOES(p0: int) -> bool: ...
    @staticmethod
    def glIsRenderbufferOES(p0: int) -> bool: ...
    @staticmethod
    def glLightModelxOES(p0: int, p1: int) -> None: ...
    @overload
    @staticmethod
    def glLightModelxvOES(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glLightModelxvOES(p0: int, p1: IntBuffer) -> None: ...
    @staticmethod
    def glLightxOES(p0: int, p1: int, p2: int) -> None: ...
    @overload
    @staticmethod
    def glLightxvOES(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glLightxvOES(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def glLineWidthxOES(p0: int) -> None: ...
    @overload
    @staticmethod
    def glLoadMatrixxOES(p0: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glLoadMatrixxOES(p0: Any, p1: int) -> None: ...
    @staticmethod
    def glLoadPaletteFromModelViewMatrixOES() -> None: ...
    @staticmethod
    def glMaterialxOES(p0: int, p1: int, p2: int) -> None: ...
    @overload
    @staticmethod
    def glMaterialxvOES(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glMaterialxvOES(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def glMatrixIndexPointerOES(p0: int, p1: int, p2: int, p3: Buffer) -> None: ...
    @overload
    @staticmethod
    def glMultMatrixxOES(p0: Any, p1: int) -> None: ...
    @overload
    @staticmethod
    def glMultMatrixxOES(p0: IntBuffer) -> None: ...
    @staticmethod
    def glMultiTexCoord4xOES(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @staticmethod
    def glNormal3xOES(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glOrthofOES(p0: float, p1: float, p2: float, p3: float, p4: float, p5: float) -> None: ...
    @staticmethod
    def glOrthoxOES(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int) -> None: ...
    @staticmethod
    def glPointParameterxOES(p0: int, p1: int) -> None: ...
    @overload
    @staticmethod
    def glPointParameterxvOES(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glPointParameterxvOES(p0: int, p1: IntBuffer) -> None: ...
    @staticmethod
    def glPointSizexOES(p0: int) -> None: ...
    @staticmethod
    def glPolygonOffsetxOES(p0: int, p1: int) -> None: ...
    @staticmethod
    def glRenderbufferStorageOES(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glRotatexOES(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glSampleCoveragexOES(p0: int, p1: bool) -> None: ...
    @staticmethod
    def glScalexOES(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glTexEnvxOES(p0: int, p1: int, p2: int) -> None: ...
    @overload
    @staticmethod
    def glTexEnvxvOES(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glTexEnvxvOES(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def glTexGenfOES(p0: int, p1: int, p2: float) -> None: ...
    @overload
    @staticmethod
    def glTexGenfvOES(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glTexGenfvOES(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @staticmethod
    def glTexGeniOES(p0: int, p1: int, p2: int) -> None: ...
    @overload
    @staticmethod
    def glTexGenivOES(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glTexGenivOES(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def glTexGenxOES(p0: int, p1: int, p2: int) -> None: ...
    @overload
    @staticmethod
    def glTexGenxvOES(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glTexGenxvOES(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @staticmethod
    def glTexParameterxOES(p0: int, p1: int, p2: int) -> None: ...
    @overload
    @staticmethod
    def glTexParameterxvOES(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glTexParameterxvOES(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @staticmethod
    def glTranslatexOES(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glWeightPointerOES(p0: int, p1: int, p2: int, p3: Buffer) -> None: ...

from typing import Any, ClassVar, overload
from java.nio.Buffer import Buffer
from java.nio.FloatBuffer import FloatBuffer
from java.nio.IntBuffer import IntBuffer

class GLES10:
    GL_ADD: ClassVar[int]
    GL_ALIASED_LINE_WIDTH_RANGE: ClassVar[int]
    GL_ALIASED_POINT_SIZE_RANGE: ClassVar[int]
    GL_ALPHA: ClassVar[int]
    GL_ALPHA_BITS: ClassVar[int]
    GL_ALPHA_TEST: ClassVar[int]
    GL_ALWAYS: ClassVar[int]
    GL_AMBIENT: ClassVar[int]
    GL_AMBIENT_AND_DIFFUSE: ClassVar[int]
    GL_AND: ClassVar[int]
    GL_AND_INVERTED: ClassVar[int]
    GL_AND_REVERSE: ClassVar[int]
    GL_BACK: ClassVar[int]
    GL_BLEND: ClassVar[int]
    GL_BLUE_BITS: ClassVar[int]
    GL_BYTE: ClassVar[int]
    GL_CCW: ClassVar[int]
    GL_CLAMP_TO_EDGE: ClassVar[int]
    GL_CLEAR: ClassVar[int]
    GL_COLOR_ARRAY: ClassVar[int]
    GL_COLOR_BUFFER_BIT: ClassVar[int]
    GL_COLOR_LOGIC_OP: ClassVar[int]
    GL_COLOR_MATERIAL: ClassVar[int]
    GL_COMPRESSED_TEXTURE_FORMATS: ClassVar[int]
    GL_CONSTANT_ATTENUATION: ClassVar[int]
    GL_COPY: ClassVar[int]
    GL_COPY_INVERTED: ClassVar[int]
    GL_CULL_FACE: ClassVar[int]
    GL_CW: ClassVar[int]
    GL_DECAL: ClassVar[int]
    GL_DECR: ClassVar[int]
    GL_DEPTH_BITS: ClassVar[int]
    GL_DEPTH_BUFFER_BIT: ClassVar[int]
    GL_DEPTH_TEST: ClassVar[int]
    GL_DIFFUSE: ClassVar[int]
    GL_DITHER: ClassVar[int]
    GL_DONT_CARE: ClassVar[int]
    GL_DST_ALPHA: ClassVar[int]
    GL_DST_COLOR: ClassVar[int]
    GL_EMISSION: ClassVar[int]
    GL_EQUAL: ClassVar[int]
    GL_EQUIV: ClassVar[int]
    GL_EXP: ClassVar[int]
    GL_EXP2: ClassVar[int]
    GL_EXTENSIONS: ClassVar[int]
    GL_FALSE: ClassVar[int]
    GL_FASTEST: ClassVar[int]
    GL_FIXED: ClassVar[int]
    GL_FLAT: ClassVar[int]
    GL_FLOAT: ClassVar[int]
    GL_FOG: ClassVar[int]
    GL_FOG_COLOR: ClassVar[int]
    GL_FOG_DENSITY: ClassVar[int]
    GL_FOG_END: ClassVar[int]
    GL_FOG_HINT: ClassVar[int]
    GL_FOG_MODE: ClassVar[int]
    GL_FOG_START: ClassVar[int]
    GL_FRONT: ClassVar[int]
    GL_FRONT_AND_BACK: ClassVar[int]
    GL_GEQUAL: ClassVar[int]
    GL_GREATER: ClassVar[int]
    GL_GREEN_BITS: ClassVar[int]
    GL_IMPLEMENTATION_COLOR_READ_FORMAT_OES: ClassVar[int]
    GL_IMPLEMENTATION_COLOR_READ_TYPE_OES: ClassVar[int]
    GL_INCR: ClassVar[int]
    GL_INVALID_ENUM: ClassVar[int]
    GL_INVALID_OPERATION: ClassVar[int]
    GL_INVALID_VALUE: ClassVar[int]
    GL_INVERT: ClassVar[int]
    GL_KEEP: ClassVar[int]
    GL_LEQUAL: ClassVar[int]
    GL_LESS: ClassVar[int]
    GL_LIGHT0: ClassVar[int]
    GL_LIGHT1: ClassVar[int]
    GL_LIGHT2: ClassVar[int]
    GL_LIGHT3: ClassVar[int]
    GL_LIGHT4: ClassVar[int]
    GL_LIGHT5: ClassVar[int]
    GL_LIGHT6: ClassVar[int]
    GL_LIGHT7: ClassVar[int]
    GL_LIGHTING: ClassVar[int]
    GL_LIGHT_MODEL_AMBIENT: ClassVar[int]
    GL_LIGHT_MODEL_TWO_SIDE: ClassVar[int]
    GL_LINEAR: ClassVar[int]
    GL_LINEAR_ATTENUATION: ClassVar[int]
    GL_LINEAR_MIPMAP_LINEAR: ClassVar[int]
    GL_LINEAR_MIPMAP_NEAREST: ClassVar[int]
    GL_LINES: ClassVar[int]
    GL_LINE_LOOP: ClassVar[int]
    GL_LINE_SMOOTH: ClassVar[int]
    GL_LINE_SMOOTH_HINT: ClassVar[int]
    GL_LINE_STRIP: ClassVar[int]
    GL_LUMINANCE: ClassVar[int]
    GL_LUMINANCE_ALPHA: ClassVar[int]
    GL_MAX_ELEMENTS_INDICES: ClassVar[int]
    GL_MAX_ELEMENTS_VERTICES: ClassVar[int]
    GL_MAX_LIGHTS: ClassVar[int]
    GL_MAX_MODELVIEW_STACK_DEPTH: ClassVar[int]
    GL_MAX_PROJECTION_STACK_DEPTH: ClassVar[int]
    GL_MAX_TEXTURE_SIZE: ClassVar[int]
    GL_MAX_TEXTURE_STACK_DEPTH: ClassVar[int]
    GL_MAX_TEXTURE_UNITS: ClassVar[int]
    GL_MAX_VIEWPORT_DIMS: ClassVar[int]
    GL_MODELVIEW: ClassVar[int]
    GL_MODULATE: ClassVar[int]
    GL_MULTISAMPLE: ClassVar[int]
    GL_NAND: ClassVar[int]
    GL_NEAREST: ClassVar[int]
    GL_NEAREST_MIPMAP_LINEAR: ClassVar[int]
    GL_NEAREST_MIPMAP_NEAREST: ClassVar[int]
    GL_NEVER: ClassVar[int]
    GL_NICEST: ClassVar[int]
    GL_NOOP: ClassVar[int]
    GL_NOR: ClassVar[int]
    GL_NORMALIZE: ClassVar[int]
    GL_NORMAL_ARRAY: ClassVar[int]
    GL_NOTEQUAL: ClassVar[int]
    GL_NO_ERROR: ClassVar[int]
    GL_NUM_COMPRESSED_TEXTURE_FORMATS: ClassVar[int]
    GL_ONE: ClassVar[int]
    GL_ONE_MINUS_DST_ALPHA: ClassVar[int]
    GL_ONE_MINUS_DST_COLOR: ClassVar[int]
    GL_ONE_MINUS_SRC_ALPHA: ClassVar[int]
    GL_ONE_MINUS_SRC_COLOR: ClassVar[int]
    GL_OR: ClassVar[int]
    GL_OR_INVERTED: ClassVar[int]
    GL_OR_REVERSE: ClassVar[int]
    GL_OUT_OF_MEMORY: ClassVar[int]
    GL_PACK_ALIGNMENT: ClassVar[int]
    GL_PALETTE4_R5_G6_B5_OES: ClassVar[int]
    GL_PALETTE4_RGB5_A1_OES: ClassVar[int]
    GL_PALETTE4_RGB8_OES: ClassVar[int]
    GL_PALETTE4_RGBA4_OES: ClassVar[int]
    GL_PALETTE4_RGBA8_OES: ClassVar[int]
    GL_PALETTE8_R5_G6_B5_OES: ClassVar[int]
    GL_PALETTE8_RGB5_A1_OES: ClassVar[int]
    GL_PALETTE8_RGB8_OES: ClassVar[int]
    GL_PALETTE8_RGBA4_OES: ClassVar[int]
    GL_PALETTE8_RGBA8_OES: ClassVar[int]
    GL_PERSPECTIVE_CORRECTION_HINT: ClassVar[int]
    GL_POINTS: ClassVar[int]
    GL_POINT_FADE_THRESHOLD_SIZE: ClassVar[int]
    GL_POINT_SIZE: ClassVar[int]
    GL_POINT_SMOOTH: ClassVar[int]
    GL_POINT_SMOOTH_HINT: ClassVar[int]
    GL_POLYGON_OFFSET_FILL: ClassVar[int]
    GL_POLYGON_SMOOTH_HINT: ClassVar[int]
    GL_POSITION: ClassVar[int]
    GL_PROJECTION: ClassVar[int]
    GL_QUADRATIC_ATTENUATION: ClassVar[int]
    GL_RED_BITS: ClassVar[int]
    GL_RENDERER: ClassVar[int]
    GL_REPEAT: ClassVar[int]
    GL_REPLACE: ClassVar[int]
    GL_RESCALE_NORMAL: ClassVar[int]
    GL_RGB: ClassVar[int]
    GL_RGBA: ClassVar[int]
    GL_SAMPLE_ALPHA_TO_COVERAGE: ClassVar[int]
    GL_SAMPLE_ALPHA_TO_ONE: ClassVar[int]
    GL_SAMPLE_COVERAGE: ClassVar[int]
    GL_SCISSOR_TEST: ClassVar[int]
    GL_SET: ClassVar[int]
    GL_SHININESS: ClassVar[int]
    GL_SHORT: ClassVar[int]
    GL_SMOOTH: ClassVar[int]
    GL_SMOOTH_LINE_WIDTH_RANGE: ClassVar[int]
    GL_SMOOTH_POINT_SIZE_RANGE: ClassVar[int]
    GL_SPECULAR: ClassVar[int]
    GL_SPOT_CUTOFF: ClassVar[int]
    GL_SPOT_DIRECTION: ClassVar[int]
    GL_SPOT_EXPONENT: ClassVar[int]
    GL_SRC_ALPHA: ClassVar[int]
    GL_SRC_ALPHA_SATURATE: ClassVar[int]
    GL_SRC_COLOR: ClassVar[int]
    GL_STACK_OVERFLOW: ClassVar[int]
    GL_STACK_UNDERFLOW: ClassVar[int]
    GL_STENCIL_BITS: ClassVar[int]
    GL_STENCIL_BUFFER_BIT: ClassVar[int]
    GL_STENCIL_TEST: ClassVar[int]
    GL_SUBPIXEL_BITS: ClassVar[int]
    GL_TEXTURE: ClassVar[int]
    GL_TEXTURE0: ClassVar[int]
    GL_TEXTURE1: ClassVar[int]
    GL_TEXTURE10: ClassVar[int]
    GL_TEXTURE11: ClassVar[int]
    GL_TEXTURE12: ClassVar[int]
    GL_TEXTURE13: ClassVar[int]
    GL_TEXTURE14: ClassVar[int]
    GL_TEXTURE15: ClassVar[int]
    GL_TEXTURE16: ClassVar[int]
    GL_TEXTURE17: ClassVar[int]
    GL_TEXTURE18: ClassVar[int]
    GL_TEXTURE19: ClassVar[int]
    GL_TEXTURE2: ClassVar[int]
    GL_TEXTURE20: ClassVar[int]
    GL_TEXTURE21: ClassVar[int]
    GL_TEXTURE22: ClassVar[int]
    GL_TEXTURE23: ClassVar[int]
    GL_TEXTURE24: ClassVar[int]
    GL_TEXTURE25: ClassVar[int]
    GL_TEXTURE26: ClassVar[int]
    GL_TEXTURE27: ClassVar[int]
    GL_TEXTURE28: ClassVar[int]
    GL_TEXTURE29: ClassVar[int]
    GL_TEXTURE3: ClassVar[int]
    GL_TEXTURE30: ClassVar[int]
    GL_TEXTURE31: ClassVar[int]
    GL_TEXTURE4: ClassVar[int]
    GL_TEXTURE5: ClassVar[int]
    GL_TEXTURE6: ClassVar[int]
    GL_TEXTURE7: ClassVar[int]
    GL_TEXTURE8: ClassVar[int]
    GL_TEXTURE9: ClassVar[int]
    GL_TEXTURE_2D: ClassVar[int]
    GL_TEXTURE_COORD_ARRAY: ClassVar[int]
    GL_TEXTURE_ENV: ClassVar[int]
    GL_TEXTURE_ENV_COLOR: ClassVar[int]
    GL_TEXTURE_ENV_MODE: ClassVar[int]
    GL_TEXTURE_MAG_FILTER: ClassVar[int]
    GL_TEXTURE_MIN_FILTER: ClassVar[int]
    GL_TEXTURE_WRAP_S: ClassVar[int]
    GL_TEXTURE_WRAP_T: ClassVar[int]
    GL_TRIANGLES: ClassVar[int]
    GL_TRIANGLE_FAN: ClassVar[int]
    GL_TRIANGLE_STRIP: ClassVar[int]
    GL_TRUE: ClassVar[int]
    GL_UNPACK_ALIGNMENT: ClassVar[int]
    GL_UNSIGNED_BYTE: ClassVar[int]
    GL_UNSIGNED_SHORT: ClassVar[int]
    GL_UNSIGNED_SHORT_4_4_4_4: ClassVar[int]
    GL_UNSIGNED_SHORT_5_5_5_1: ClassVar[int]
    GL_UNSIGNED_SHORT_5_6_5: ClassVar[int]
    GL_VENDOR: ClassVar[int]
    GL_VERSION: ClassVar[int]
    GL_VERTEX_ARRAY: ClassVar[int]
    GL_XOR: ClassVar[int]
    GL_ZERO: ClassVar[int]
    def __init__(self) -> None: ...
    @staticmethod
    def glHint(p0: int, p1: int) -> None: ...
    @staticmethod
    def glFogf(p0: int, p1: float) -> None: ...
    @staticmethod
    def glFogx(p0: int, p1: int) -> None: ...
    @staticmethod
    def glActiveTexture(p0: int) -> None: ...
    @staticmethod
    def glAlphaFunc(p0: int, p1: float) -> None: ...
    @staticmethod
    def glAlphaFuncx(p0: int, p1: int) -> None: ...
    @staticmethod
    def glBindTexture(p0: int, p1: int) -> None: ...
    @staticmethod
    def glBlendFunc(p0: int, p1: int) -> None: ...
    @staticmethod
    def glClear(p0: int) -> None: ...
    @staticmethod
    def glClearColor(p0: float, p1: float, p2: float, p3: float) -> None: ...
    @staticmethod
    def glClearColorx(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glClearDepthf(p0: float) -> None: ...
    @staticmethod
    def glClearDepthx(p0: int) -> None: ...
    @staticmethod
    def glClearStencil(p0: int) -> None: ...
    @staticmethod
    def glClientActiveTexture(p0: int) -> None: ...
    @staticmethod
    def glColor4f(p0: float, p1: float, p2: float, p3: float) -> None: ...
    @staticmethod
    def glColor4x(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glColorMask(p0: bool, p1: bool, p2: bool, p3: bool) -> None: ...
    @staticmethod
    def glColorPointer(p0: int, p1: int, p2: int, p3: Buffer) -> None: ...
    @staticmethod
    def glCompressedTexImage2D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: Buffer) -> None: ...
    @staticmethod
    def glCompressedTexSubImage2D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: Buffer) -> None: ...
    @staticmethod
    def glCopyTexImage2D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int) -> None: ...
    @staticmethod
    def glCopyTexSubImage2D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int) -> None: ...
    @staticmethod
    def glCullFace(p0: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteTextures(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteTextures(p0: int, p1: IntBuffer) -> None: ...
    @staticmethod
    def glDepthFunc(p0: int) -> None: ...
    @staticmethod
    def glDepthMask(p0: bool) -> None: ...
    @staticmethod
    def glDepthRangef(p0: float, p1: float) -> None: ...
    @staticmethod
    def glDepthRangex(p0: int, p1: int) -> None: ...
    @staticmethod
    def glDisable(p0: int) -> None: ...
    @staticmethod
    def glDisableClientState(p0: int) -> None: ...
    @staticmethod
    def glDrawArrays(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glDrawElements(p0: int, p1: int, p2: int, p3: Buffer) -> None: ...
    @staticmethod
    def glEnable(p0: int) -> None: ...
    @staticmethod
    def glEnableClientState(p0: int) -> None: ...
    @staticmethod
    def glFinish() -> None: ...
    @staticmethod
    def glFlush() -> None: ...
    @overload
    @staticmethod
    def glFogfv(p0: int, p1: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glFogfv(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glFogxv(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glFogxv(p0: int, p1: Any, p2: int) -> None: ...
    @staticmethod
    def glFrontFace(p0: int) -> None: ...
    @staticmethod
    def glFrustumf(p0: float, p1: float, p2: float, p3: float, p4: float, p5: float) -> None: ...
    @staticmethod
    def glFrustumx(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int) -> None: ...
    @overload
    @staticmethod
    def glGenTextures(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGenTextures(p0: int, p1: Any, p2: int) -> None: ...
    @staticmethod
    def glGetError() -> int: ...
    @overload
    @staticmethod
    def glGetIntegerv(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetIntegerv(p0: int, p1: Any, p2: int) -> None: ...
    @staticmethod
    def glGetString(p0: int) -> str: ...
    @staticmethod
    def glLightModelf(p0: int, p1: float) -> None: ...
    @overload
    @staticmethod
    def glLightModelfv(p0: int, p1: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glLightModelfv(p0: int, p1: Any, p2: int) -> None: ...
    @staticmethod
    def glLightModelx(p0: int, p1: int) -> None: ...
    @overload
    @staticmethod
    def glLightModelxv(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glLightModelxv(p0: int, p1: IntBuffer) -> None: ...
    @staticmethod
    def glLightf(p0: int, p1: int, p2: float) -> None: ...
    @overload
    @staticmethod
    def glLightfv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glLightfv(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @staticmethod
    def glLightx(p0: int, p1: int, p2: int) -> None: ...
    @overload
    @staticmethod
    def glLightxv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glLightxv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def glLineWidth(p0: float) -> None: ...
    @staticmethod
    def glLineWidthx(p0: int) -> None: ...
    @staticmethod
    def glLoadIdentity() -> None: ...
    @overload
    @staticmethod
    def glLoadMatrixf(p0: Any, p1: int) -> None: ...
    @overload
    @staticmethod
    def glLoadMatrixf(p0: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glLoadMatrixx(p0: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glLoadMatrixx(p0: Any, p1: int) -> None: ...
    @staticmethod
    def glLogicOp(p0: int) -> None: ...
    @staticmethod
    def glMaterialf(p0: int, p1: int, p2: float) -> None: ...
    @overload
    @staticmethod
    def glMaterialfv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glMaterialfv(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @staticmethod
    def glMaterialx(p0: int, p1: int, p2: int) -> None: ...
    @overload
    @staticmethod
    def glMaterialxv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glMaterialxv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @staticmethod
    def glMatrixMode(p0: int) -> None: ...
    @overload
    @staticmethod
    def glMultMatrixf(p0: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glMultMatrixf(p0: Any, p1: int) -> None: ...
    @overload
    @staticmethod
    def glMultMatrixx(p0: Any, p1: int) -> None: ...
    @overload
    @staticmethod
    def glMultMatrixx(p0: IntBuffer) -> None: ...
    @staticmethod
    def glMultiTexCoord4f(p0: int, p1: float, p2: float, p3: float, p4: float) -> None: ...
    @staticmethod
    def glMultiTexCoord4x(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @staticmethod
    def glNormal3f(p0: float, p1: float, p2: float) -> None: ...
    @staticmethod
    def glNormal3x(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glNormalPointer(p0: int, p1: int, p2: Buffer) -> None: ...
    @staticmethod
    def glOrthof(p0: float, p1: float, p2: float, p3: float, p4: float, p5: float) -> None: ...
    @staticmethod
    def glOrthox(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int) -> None: ...
    @staticmethod
    def glPixelStorei(p0: int, p1: int) -> None: ...
    @staticmethod
    def glPointSize(p0: float) -> None: ...
    @staticmethod
    def glPointSizex(p0: int) -> None: ...
    @staticmethod
    def glPolygonOffset(p0: float, p1: float) -> None: ...
    @staticmethod
    def glPolygonOffsetx(p0: int, p1: int) -> None: ...
    @staticmethod
    def glPopMatrix() -> None: ...
    @staticmethod
    def glPushMatrix() -> None: ...
    @staticmethod
    def glReadPixels(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: Buffer) -> None: ...
    @staticmethod
    def glRotatef(p0: float, p1: float, p2: float, p3: float) -> None: ...
    @staticmethod
    def glRotatex(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glSampleCoverage(p0: float, p1: bool) -> None: ...
    @staticmethod
    def glSampleCoveragex(p0: int, p1: bool) -> None: ...
    @staticmethod
    def glScalef(p0: float, p1: float, p2: float) -> None: ...
    @staticmethod
    def glScalex(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glScissor(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glShadeModel(p0: int) -> None: ...
    @staticmethod
    def glStencilFunc(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glStencilMask(p0: int) -> None: ...
    @staticmethod
    def glStencilOp(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glTexCoordPointer(p0: int, p1: int, p2: int, p3: Buffer) -> None: ...
    @staticmethod
    def glTexEnvf(p0: int, p1: int, p2: float) -> None: ...
    @overload
    @staticmethod
    def glTexEnvfv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glTexEnvfv(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @staticmethod
    def glTexEnvx(p0: int, p1: int, p2: int) -> None: ...
    @overload
    @staticmethod
    def glTexEnvxv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glTexEnvxv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @staticmethod
    def glTexImage2D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: Buffer) -> None: ...
    @staticmethod
    def glTexParameterf(p0: int, p1: int, p2: float) -> None: ...
    @staticmethod
    def glTexParameterx(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glTexSubImage2D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: Buffer) -> None: ...
    @staticmethod
    def glTranslatef(p0: float, p1: float, p2: float) -> None: ...
    @staticmethod
    def glTranslatex(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glVertexPointer(p0: int, p1: int, p2: int, p3: Buffer) -> None: ...
    @staticmethod
    def glViewport(p0: int, p1: int, p2: int, p3: int) -> None: ...

from typing import Any, ClassVar, overload
from javax.microedition.khronos.opengles.GL10 import GL10

class GLU:
    def __init__(self) -> None: ...
    @staticmethod
    def gluErrorString(p0: int) -> str: ...
    @staticmethod
    def gluLookAt(p0: GL10, p1: float, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float, p8: float, p9: float) -> None: ...
    @staticmethod
    def gluOrtho2D(p0: GL10, p1: float, p2: float, p3: float, p4: float) -> None: ...
    @staticmethod
    def gluPerspective(p0: GL10, p1: float, p2: float, p3: float, p4: float) -> None: ...
    @staticmethod
    def gluProject(p0: float, p1: float, p2: float, p3: Any, p4: int, p5: Any, p6: int, p7: Any, p8: int, p9: Any, p10: int) -> int: ...
    @staticmethod
    def gluUnProject(p0: float, p1: float, p2: float, p3: Any, p4: int, p5: Any, p6: int, p7: Any, p8: int, p9: Any, p10: int) -> int: ...

from typing import Any, ClassVar, overload

class EGLObjectHandle:
    def getNativeHandle(self) -> int: ...
    def hashCode(self) -> int: ...
    def getHandle(self) -> int: ...

from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.util.AttributeSet import AttributeSet
from android.util.Property import Property
from android.view.SurfaceHolder import SurfaceHolder
from java.lang.Runnable import Runnable
from javax.microedition.khronos.egl.EGL10 import EGL10
from javax.microedition.khronos.egl.EGLConfig import EGLConfig
from javax.microedition.khronos.egl.EGLContext import EGLContext
from javax.microedition.khronos.egl.EGLDisplay import EGLDisplay
from javax.microedition.khronos.egl.EGLSurface import EGLSurface
from javax.microedition.khronos.opengles.GL import GL
from javax.microedition.khronos.opengles.GL10 import GL10

class GLSurfaceView:
    DEBUG_CHECK_GL_ERROR: ClassVar[int]
    DEBUG_LOG_GL_CALLS: ClassVar[int]
    RENDERMODE_CONTINUOUSLY: ClassVar[int]
    RENDERMODE_WHEN_DIRTY: ClassVar[int]
    SURFACE_LIFECYCLE_DEFAULT: ClassVar[int]
    SURFACE_LIFECYCLE_FOLLOWS_ATTACHMENT: ClassVar[int]
    SURFACE_LIFECYCLE_FOLLOWS_VISIBILITY: ClassVar[int]
    ACCESSIBILITY_DATA_SENSITIVE_AUTO: ClassVar[int]
    ACCESSIBILITY_DATA_SENSITIVE_NO: ClassVar[int]
    ACCESSIBILITY_DATA_SENSITIVE_YES: ClassVar[int]
    ACCESSIBILITY_LIVE_REGION_ASSERTIVE: ClassVar[int]
    ACCESSIBILITY_LIVE_REGION_NONE: ClassVar[int]
    ACCESSIBILITY_LIVE_REGION_POLITE: ClassVar[int]
    ALPHA: ClassVar[Property]
    AUTOFILL_FLAG_INCLUDE_NOT_IMPORTANT_VIEWS: ClassVar[int]
    AUTOFILL_HINT_CREDIT_CARD_EXPIRATION_DATE: ClassVar[str]
    AUTOFILL_HINT_CREDIT_CARD_EXPIRATION_DAY: ClassVar[str]
    AUTOFILL_HINT_CREDIT_CARD_EXPIRATION_MONTH: ClassVar[str]
    AUTOFILL_HINT_CREDIT_CARD_EXPIRATION_YEAR: ClassVar[str]
    AUTOFILL_HINT_CREDIT_CARD_NUMBER: ClassVar[str]
    AUTOFILL_HINT_CREDIT_CARD_SECURITY_CODE: ClassVar[str]
    AUTOFILL_HINT_EMAIL_ADDRESS: ClassVar[str]
    AUTOFILL_HINT_NAME: ClassVar[str]
    AUTOFILL_HINT_PASSWORD: ClassVar[str]
    AUTOFILL_HINT_PHONE: ClassVar[str]
    AUTOFILL_HINT_POSTAL_ADDRESS: ClassVar[str]
    AUTOFILL_HINT_POSTAL_CODE: ClassVar[str]
    AUTOFILL_HINT_USERNAME: ClassVar[str]
    AUTOFILL_TYPE_DATE: ClassVar[int]
    AUTOFILL_TYPE_LIST: ClassVar[int]
    AUTOFILL_TYPE_NONE: ClassVar[int]
    AUTOFILL_TYPE_TEXT: ClassVar[int]
    AUTOFILL_TYPE_TOGGLE: ClassVar[int]
    CONTENT_SENSITIVITY_AUTO: ClassVar[int]
    CONTENT_SENSITIVITY_NOT_SENSITIVE: ClassVar[int]
    CONTENT_SENSITIVITY_SENSITIVE: ClassVar[int]
    DRAG_FLAG_ACCESSIBILITY_ACTION: ClassVar[int]
    DRAG_FLAG_GLOBAL: ClassVar[int]
    DRAG_FLAG_GLOBAL_PERSISTABLE_URI_PERMISSION: ClassVar[int]
    DRAG_FLAG_GLOBAL_PREFIX_URI_PERMISSION: ClassVar[int]
    DRAG_FLAG_GLOBAL_SAME_APPLICATION: ClassVar[int]
    DRAG_FLAG_GLOBAL_URI_READ: ClassVar[int]
    DRAG_FLAG_GLOBAL_URI_WRITE: ClassVar[int]
    DRAG_FLAG_HIDE_CALLING_TASK_ON_DRAG_START: ClassVar[int]
    DRAG_FLAG_OPAQUE: ClassVar[int]
    DRAG_FLAG_START_INTENT_SENDER_ON_UNHANDLED_DRAG: ClassVar[int]
    DRAWING_CACHE_QUALITY_AUTO: ClassVar[int]
    DRAWING_CACHE_QUALITY_HIGH: ClassVar[int]
    DRAWING_CACHE_QUALITY_LOW: ClassVar[int]
    FIND_VIEWS_WITH_CONTENT_DESCRIPTION: ClassVar[int]
    FIND_VIEWS_WITH_TEXT: ClassVar[int]
    FOCUSABLE: ClassVar[int]
    FOCUSABLES_ALL: ClassVar[int]
    FOCUSABLES_TOUCH_MODE: ClassVar[int]
    FOCUSABLE_AUTO: ClassVar[int]
    FOCUS_BACKWARD: ClassVar[int]
    FOCUS_DOWN: ClassVar[int]
    FOCUS_FORWARD: ClassVar[int]
    FOCUS_LEFT: ClassVar[int]
    FOCUS_RIGHT: ClassVar[int]
    FOCUS_UP: ClassVar[int]
    GONE: ClassVar[int]
    HAPTIC_FEEDBACK_ENABLED: ClassVar[int]
    IMPORTANT_FOR_ACCESSIBILITY_AUTO: ClassVar[int]
    IMPORTANT_FOR_ACCESSIBILITY_NO: ClassVar[int]
    IMPORTANT_FOR_ACCESSIBILITY_NO_HIDE_DESCENDANTS: ClassVar[int]
    IMPORTANT_FOR_ACCESSIBILITY_YES: ClassVar[int]
    IMPORTANT_FOR_AUTOFILL_AUTO: ClassVar[int]
    IMPORTANT_FOR_AUTOFILL_NO: ClassVar[int]
    IMPORTANT_FOR_AUTOFILL_NO_EXCLUDE_DESCENDANTS: ClassVar[int]
    IMPORTANT_FOR_AUTOFILL_YES: ClassVar[int]
    IMPORTANT_FOR_AUTOFILL_YES_EXCLUDE_DESCENDANTS: ClassVar[int]
    IMPORTANT_FOR_CONTENT_CAPTURE_AUTO: ClassVar[int]
    IMPORTANT_FOR_CONTENT_CAPTURE_NO: ClassVar[int]
    IMPORTANT_FOR_CONTENT_CAPTURE_NO_EXCLUDE_DESCENDANTS: ClassVar[int]
    IMPORTANT_FOR_CONTENT_CAPTURE_YES: ClassVar[int]
    IMPORTANT_FOR_CONTENT_CAPTURE_YES_EXCLUDE_DESCENDANTS: ClassVar[int]
    INVISIBLE: ClassVar[int]
    KEEP_SCREEN_ON: ClassVar[int]
    LAYER_TYPE_HARDWARE: ClassVar[int]
    LAYER_TYPE_NONE: ClassVar[int]
    LAYER_TYPE_SOFTWARE: ClassVar[int]
    LAYOUT_DIRECTION_INHERIT: ClassVar[int]
    LAYOUT_DIRECTION_LOCALE: ClassVar[int]
    LAYOUT_DIRECTION_LTR: ClassVar[int]
    LAYOUT_DIRECTION_RTL: ClassVar[int]
    MEASURED_HEIGHT_STATE_SHIFT: ClassVar[int]
    MEASURED_SIZE_MASK: ClassVar[int]
    MEASURED_STATE_MASK: ClassVar[int]
    MEASURED_STATE_TOO_SMALL: ClassVar[int]
    NOT_FOCUSABLE: ClassVar[int]
    NO_ID: ClassVar[int]
    OVER_SCROLL_ALWAYS: ClassVar[int]
    OVER_SCROLL_IF_CONTENT_SCROLLS: ClassVar[int]
    OVER_SCROLL_NEVER: ClassVar[int]
    REQUESTED_FRAME_RATE_CATEGORY_DEFAULT: ClassVar[float]
    REQUESTED_FRAME_RATE_CATEGORY_HIGH: ClassVar[float]
    REQUESTED_FRAME_RATE_CATEGORY_LOW: ClassVar[float]
    REQUESTED_FRAME_RATE_CATEGORY_NORMAL: ClassVar[float]
    REQUESTED_FRAME_RATE_CATEGORY_NO_PREFERENCE: ClassVar[float]
    ROTATION: ClassVar[Property]
    ROTATION_X: ClassVar[Property]
    ROTATION_Y: ClassVar[Property]
    SCALE_X: ClassVar[Property]
    SCALE_Y: ClassVar[Property]
    SCREEN_STATE_OFF: ClassVar[int]
    SCREEN_STATE_ON: ClassVar[int]
    SCROLLBARS_INSIDE_INSET: ClassVar[int]
    SCROLLBARS_INSIDE_OVERLAY: ClassVar[int]
    SCROLLBARS_OUTSIDE_INSET: ClassVar[int]
    SCROLLBARS_OUTSIDE_OVERLAY: ClassVar[int]
    SCROLLBAR_POSITION_DEFAULT: ClassVar[int]
    SCROLLBAR_POSITION_LEFT: ClassVar[int]
    SCROLLBAR_POSITION_RIGHT: ClassVar[int]
    SCROLL_AXIS_HORIZONTAL: ClassVar[int]
    SCROLL_AXIS_NONE: ClassVar[int]
    SCROLL_AXIS_VERTICAL: ClassVar[int]
    SCROLL_CAPTURE_HINT_AUTO: ClassVar[int]
    SCROLL_CAPTURE_HINT_EXCLUDE: ClassVar[int]
    SCROLL_CAPTURE_HINT_EXCLUDE_DESCENDANTS: ClassVar[int]
    SCROLL_CAPTURE_HINT_INCLUDE: ClassVar[int]
    SCROLL_INDICATOR_BOTTOM: ClassVar[int]
    SCROLL_INDICATOR_END: ClassVar[int]
    SCROLL_INDICATOR_LEFT: ClassVar[int]
    SCROLL_INDICATOR_RIGHT: ClassVar[int]
    SCROLL_INDICATOR_START: ClassVar[int]
    SCROLL_INDICATOR_TOP: ClassVar[int]
    SOUND_EFFECTS_ENABLED: ClassVar[int]
    STATUS_BAR_HIDDEN: ClassVar[int]
    STATUS_BAR_VISIBLE: ClassVar[int]
    SYSTEM_UI_FLAG_FULLSCREEN: ClassVar[int]
    SYSTEM_UI_FLAG_HIDE_NAVIGATION: ClassVar[int]
    SYSTEM_UI_FLAG_IMMERSIVE: ClassVar[int]
    SYSTEM_UI_FLAG_IMMERSIVE_STICKY: ClassVar[int]
    SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN: ClassVar[int]
    SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION: ClassVar[int]
    SYSTEM_UI_FLAG_LAYOUT_STABLE: ClassVar[int]
    SYSTEM_UI_FLAG_LIGHT_NAVIGATION_BAR: ClassVar[int]
    SYSTEM_UI_FLAG_LIGHT_STATUS_BAR: ClassVar[int]
    SYSTEM_UI_FLAG_LOW_PROFILE: ClassVar[int]
    SYSTEM_UI_FLAG_VISIBLE: ClassVar[int]
    SYSTEM_UI_LAYOUT_FLAGS: ClassVar[int]
    TEXT_ALIGNMENT_CENTER: ClassVar[int]
    TEXT_ALIGNMENT_GRAVITY: ClassVar[int]
    TEXT_ALIGNMENT_INHERIT: ClassVar[int]
    TEXT_ALIGNMENT_TEXT_END: ClassVar[int]
    TEXT_ALIGNMENT_TEXT_START: ClassVar[int]
    TEXT_ALIGNMENT_VIEW_END: ClassVar[int]
    TEXT_ALIGNMENT_VIEW_START: ClassVar[int]
    TEXT_DIRECTION_ANY_RTL: ClassVar[int]
    TEXT_DIRECTION_FIRST_STRONG: ClassVar[int]
    TEXT_DIRECTION_FIRST_STRONG_LTR: ClassVar[int]
    TEXT_DIRECTION_FIRST_STRONG_RTL: ClassVar[int]
    TEXT_DIRECTION_INHERIT: ClassVar[int]
    TEXT_DIRECTION_LOCALE: ClassVar[int]
    TEXT_DIRECTION_LTR: ClassVar[int]
    TEXT_DIRECTION_RTL: ClassVar[int]
    TRANSLATION_X: ClassVar[Property]
    TRANSLATION_Y: ClassVar[Property]
    TRANSLATION_Z: ClassVar[Property]
    VISIBLE: ClassVar[int]
    X: ClassVar[Property]
    Y: ClassVar[Property]
    Z: ClassVar[Property]
    @overload
    def __init__(self, p0: Context, p1: AttributeSet) -> None: ...
    @overload
    def __init__(self, p0: Context) -> None: ...
    def surfaceChanged(self, p0: SurfaceHolder, p1: int, p2: int, p3: int) -> None: ...
    def surfaceRedrawNeeded(self, p0: SurfaceHolder) -> None: ...
    def surfaceRedrawNeededAsync(self, p0: SurfaceHolder, p1: Runnable) -> None: ...
    def surfaceCreated(self, p0: SurfaceHolder) -> None: ...
    def surfaceDestroyed(self, p0: SurfaceHolder) -> None: ...
    def getRenderMode(self) -> int: ...
    def getDebugFlags(self) -> int: ...
    def getPreserveEGLContextOnPause(self) -> bool: ...
    def queueEvent(self, p0: Runnable) -> None: ...
    def requestRender(self) -> None: ...
    def setDebugFlags(self, p0: int) -> None: ...
    @overload
    def setEGLConfigChooser(self, p0: Any) -> None: ...
    @overload
    def setEGLConfigChooser(self, p0: bool) -> None: ...
    @overload
    def setEGLConfigChooser(self, p0: int, p1: int, p2: int, p3: int, p4: int, p5: int) -> None: ...
    def setEGLContextClientVersion(self, p0: int) -> None: ...
    def setEGLContextFactory(self, p0: Any) -> None: ...
    def setEGLWindowSurfaceFactory(self, p0: Any) -> None: ...
    def setGLWrapper(self, p0: Any) -> None: ...
    def setPreserveEGLContextOnPause(self, p0: bool) -> None: ...
    def setRenderMode(self, p0: int) -> None: ...
    def setRenderer(self, p0: Any) -> None: ...
    def onPause(self) -> None: ...
    def onResume(self) -> None: ...

    class Renderer:
        def onDrawFrame(self, p0: GL10) -> None: ...
        def onSurfaceChanged(self, p0: GL10, p1: int, p2: int) -> None: ...
        def onSurfaceCreated(self, p0: GL10, p1: EGLConfig) -> None: ...

    class GLWrapper:
        def wrap(self, p0: GL) -> GL: ...

    class EGLWindowSurfaceFactory:
        def createWindowSurface(self, p0: EGL10, p1: EGLDisplay, p2: EGLConfig, p3: Any) -> EGLSurface: ...
        def destroySurface(self, p0: EGL10, p1: EGLDisplay, p2: EGLSurface) -> None: ...

    class EGLContextFactory:
        def destroyContext(self, p0: EGL10, p1: EGLDisplay, p2: EGLContext) -> None: ...
        def createContext(self, p0: EGL10, p1: EGLDisplay, p2: EGLConfig) -> EGLContext: ...

    class EGLConfigChooser:
        def chooseConfig(self, p0: EGL10, p1: EGLDisplay) -> EGLConfig: ...

from typing import Any, ClassVar, overload

class Visibility:
    def __init__(self) -> None: ...
    @staticmethod
    def frustumCullSpheres(p0: Any, p1: int, p2: Any, p3: int, p4: int, p5: Any, p6: int, p7: int) -> int: ...
    @staticmethod
    def computeBoundingSphere(p0: Any, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @staticmethod
    def visibilityTest(p0: Any, p1: int, p2: Any, p3: int, p4: Any, p5: int, p6: int) -> int: ...

from typing import Any, ClassVar, overload

class EGLSync:
    def equals(self, p0: Any) -> bool: ...

from typing import Any, ClassVar, overload
from java.io.InputStream import InputStream
from java.io.OutputStream import OutputStream
from java.nio.Buffer import Buffer
from java.nio.ByteBuffer import ByteBuffer

class ETC1Util:
    def __init__(self) -> None: ...
    @staticmethod
    def compressTexture(p0: Buffer, p1: int, p2: int, p3: int, p4: int) -> Any: ...
    @staticmethod
    def isETC1Supported() -> bool: ...
    @overload
    @staticmethod
    def loadTexture(p0: int, p1: int, p2: int, p3: int, p4: int, p5: InputStream) -> None: ...
    @overload
    @staticmethod
    def loadTexture(p0: int, p1: int, p2: int, p3: int, p4: int, p5: Any) -> None: ...
    @staticmethod
    def createTexture(p0: InputStream) -> Any: ...
    @staticmethod
    def writeTexture(p0: Any, p1: OutputStream) -> None: ...

    class ETC1Texture:
        def __init__(self, p0: int, p1: int, p2: ByteBuffer) -> None: ...
        def getData(self) -> ByteBuffer: ...
        def getHeight(self) -> int: ...
        def getWidth(self) -> int: ...

from typing import Any, ClassVar, overload
from android.graphics.Bitmap import Bitmap

class GLUtils:
    @staticmethod
    def getEGLErrorString(p0: int) -> str: ...
    @overload
    @staticmethod
    def texImage2D(p0: int, p1: int, p2: int, p3: Bitmap, p4: int, p5: int) -> None: ...
    @overload
    @staticmethod
    def texImage2D(p0: int, p1: int, p2: int, p3: Bitmap, p4: int) -> None: ...
    @overload
    @staticmethod
    def texImage2D(p0: int, p1: int, p2: Bitmap, p3: int) -> None: ...
    @staticmethod
    def getInternalFormat(p0: Bitmap) -> int: ...
    @overload
    @staticmethod
    def texSubImage2D(p0: int, p1: int, p2: int, p3: int, p4: Bitmap) -> None: ...
    @overload
    @staticmethod
    def texSubImage2D(p0: int, p1: int, p2: int, p3: int, p4: Bitmap, p5: int, p6: int) -> None: ...
    @staticmethod
    def getType(p0: Bitmap) -> int: ...

from typing import Any, ClassVar, overload

class EGLConfig:
    def equals(self, p0: Any) -> bool: ...

from typing import Any, ClassVar, overload
from java.nio.Buffer import Buffer
from java.nio.ByteBuffer import ByteBuffer
from java.nio.FloatBuffer import FloatBuffer
from java.nio.IntBuffer import IntBuffer

class GLES32:
    GL_BUFFER: ClassVar[int]
    GL_CLAMP_TO_BORDER: ClassVar[int]
    GL_COLORBURN: ClassVar[int]
    GL_COLORDODGE: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_10x10: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_10x5: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_10x6: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_10x8: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_12x10: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_12x12: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_4x4: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_5x4: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_5x5: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_6x5: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_6x6: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_8x5: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_8x6: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_8x8: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x10: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x5: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x6: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x8: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_12x10: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_12x12: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_4x4: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_5x4: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_5x5: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_6x5: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_6x6: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x5: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x6: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x8: ClassVar[int]
    GL_CONTEXT_FLAGS: ClassVar[int]
    GL_CONTEXT_FLAG_DEBUG_BIT: ClassVar[int]
    GL_CONTEXT_FLAG_ROBUST_ACCESS_BIT: ClassVar[int]
    GL_CONTEXT_LOST: ClassVar[int]
    GL_DARKEN: ClassVar[int]
    GL_DEBUG_CALLBACK_FUNCTION: ClassVar[int]
    GL_DEBUG_CALLBACK_USER_PARAM: ClassVar[int]
    GL_DEBUG_GROUP_STACK_DEPTH: ClassVar[int]
    GL_DEBUG_LOGGED_MESSAGES: ClassVar[int]
    GL_DEBUG_NEXT_LOGGED_MESSAGE_LENGTH: ClassVar[int]
    GL_DEBUG_OUTPUT: ClassVar[int]
    GL_DEBUG_OUTPUT_SYNCHRONOUS: ClassVar[int]
    GL_DEBUG_SEVERITY_HIGH: ClassVar[int]
    GL_DEBUG_SEVERITY_LOW: ClassVar[int]
    GL_DEBUG_SEVERITY_MEDIUM: ClassVar[int]
    GL_DEBUG_SEVERITY_NOTIFICATION: ClassVar[int]
    GL_DEBUG_SOURCE_API: ClassVar[int]
    GL_DEBUG_SOURCE_APPLICATION: ClassVar[int]
    GL_DEBUG_SOURCE_OTHER: ClassVar[int]
    GL_DEBUG_SOURCE_SHADER_COMPILER: ClassVar[int]
    GL_DEBUG_SOURCE_THIRD_PARTY: ClassVar[int]
    GL_DEBUG_SOURCE_WINDOW_SYSTEM: ClassVar[int]
    GL_DEBUG_TYPE_DEPRECATED_BEHAVIOR: ClassVar[int]
    GL_DEBUG_TYPE_ERROR: ClassVar[int]
    GL_DEBUG_TYPE_MARKER: ClassVar[int]
    GL_DEBUG_TYPE_OTHER: ClassVar[int]
    GL_DEBUG_TYPE_PERFORMANCE: ClassVar[int]
    GL_DEBUG_TYPE_POP_GROUP: ClassVar[int]
    GL_DEBUG_TYPE_PORTABILITY: ClassVar[int]
    GL_DEBUG_TYPE_PUSH_GROUP: ClassVar[int]
    GL_DEBUG_TYPE_UNDEFINED_BEHAVIOR: ClassVar[int]
    GL_DIFFERENCE: ClassVar[int]
    GL_EXCLUSION: ClassVar[int]
    GL_FIRST_VERTEX_CONVENTION: ClassVar[int]
    GL_FRACTIONAL_EVEN: ClassVar[int]
    GL_FRACTIONAL_ODD: ClassVar[int]
    GL_FRAGMENT_INTERPOLATION_OFFSET_BITS: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_LAYERED: ClassVar[int]
    GL_FRAMEBUFFER_DEFAULT_LAYERS: ClassVar[int]
    GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS: ClassVar[int]
    GL_GEOMETRY_INPUT_TYPE: ClassVar[int]
    GL_GEOMETRY_OUTPUT_TYPE: ClassVar[int]
    GL_GEOMETRY_SHADER: ClassVar[int]
    GL_GEOMETRY_SHADER_BIT: ClassVar[int]
    GL_GEOMETRY_SHADER_INVOCATIONS: ClassVar[int]
    GL_GEOMETRY_VERTICES_OUT: ClassVar[int]
    GL_GUILTY_CONTEXT_RESET: ClassVar[int]
    GL_HARDLIGHT: ClassVar[int]
    GL_HSL_COLOR: ClassVar[int]
    GL_HSL_HUE: ClassVar[int]
    GL_HSL_LUMINOSITY: ClassVar[int]
    GL_HSL_SATURATION: ClassVar[int]
    GL_IMAGE_BUFFER: ClassVar[int]
    GL_IMAGE_CUBE_MAP_ARRAY: ClassVar[int]
    GL_INNOCENT_CONTEXT_RESET: ClassVar[int]
    GL_INT_IMAGE_BUFFER: ClassVar[int]
    GL_INT_IMAGE_CUBE_MAP_ARRAY: ClassVar[int]
    GL_INT_SAMPLER_2D_MULTISAMPLE_ARRAY: ClassVar[int]
    GL_INT_SAMPLER_BUFFER: ClassVar[int]
    GL_INT_SAMPLER_CUBE_MAP_ARRAY: ClassVar[int]
    GL_ISOLINES: ClassVar[int]
    GL_IS_PER_PATCH: ClassVar[int]
    GL_LAST_VERTEX_CONVENTION: ClassVar[int]
    GL_LAYER_PROVOKING_VERTEX: ClassVar[int]
    GL_LIGHTEN: ClassVar[int]
    GL_LINES_ADJACENCY: ClassVar[int]
    GL_LINE_STRIP_ADJACENCY: ClassVar[int]
    GL_LOSE_CONTEXT_ON_RESET: ClassVar[int]
    GL_MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS: ClassVar[int]
    GL_MAX_COMBINED_TESS_CONTROL_UNIFORM_COMPONENTS: ClassVar[int]
    GL_MAX_COMBINED_TESS_EVALUATION_UNIFORM_COMPONENTS: ClassVar[int]
    GL_MAX_DEBUG_GROUP_STACK_DEPTH: ClassVar[int]
    GL_MAX_DEBUG_LOGGED_MESSAGES: ClassVar[int]
    GL_MAX_DEBUG_MESSAGE_LENGTH: ClassVar[int]
    GL_MAX_FRAGMENT_INTERPOLATION_OFFSET: ClassVar[int]
    GL_MAX_FRAMEBUFFER_LAYERS: ClassVar[int]
    GL_MAX_GEOMETRY_ATOMIC_COUNTERS: ClassVar[int]
    GL_MAX_GEOMETRY_ATOMIC_COUNTER_BUFFERS: ClassVar[int]
    GL_MAX_GEOMETRY_IMAGE_UNIFORMS: ClassVar[int]
    GL_MAX_GEOMETRY_INPUT_COMPONENTS: ClassVar[int]
    GL_MAX_GEOMETRY_OUTPUT_COMPONENTS: ClassVar[int]
    GL_MAX_GEOMETRY_OUTPUT_VERTICES: ClassVar[int]
    GL_MAX_GEOMETRY_SHADER_INVOCATIONS: ClassVar[int]
    GL_MAX_GEOMETRY_SHADER_STORAGE_BLOCKS: ClassVar[int]
    GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS: ClassVar[int]
    GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS: ClassVar[int]
    GL_MAX_GEOMETRY_UNIFORM_BLOCKS: ClassVar[int]
    GL_MAX_GEOMETRY_UNIFORM_COMPONENTS: ClassVar[int]
    GL_MAX_LABEL_LENGTH: ClassVar[int]
    GL_MAX_PATCH_VERTICES: ClassVar[int]
    GL_MAX_TESS_CONTROL_ATOMIC_COUNTERS: ClassVar[int]
    GL_MAX_TESS_CONTROL_ATOMIC_COUNTER_BUFFERS: ClassVar[int]
    GL_MAX_TESS_CONTROL_IMAGE_UNIFORMS: ClassVar[int]
    GL_MAX_TESS_CONTROL_INPUT_COMPONENTS: ClassVar[int]
    GL_MAX_TESS_CONTROL_OUTPUT_COMPONENTS: ClassVar[int]
    GL_MAX_TESS_CONTROL_SHADER_STORAGE_BLOCKS: ClassVar[int]
    GL_MAX_TESS_CONTROL_TEXTURE_IMAGE_UNITS: ClassVar[int]
    GL_MAX_TESS_CONTROL_TOTAL_OUTPUT_COMPONENTS: ClassVar[int]
    GL_MAX_TESS_CONTROL_UNIFORM_BLOCKS: ClassVar[int]
    GL_MAX_TESS_CONTROL_UNIFORM_COMPONENTS: ClassVar[int]
    GL_MAX_TESS_EVALUATION_ATOMIC_COUNTERS: ClassVar[int]
    GL_MAX_TESS_EVALUATION_ATOMIC_COUNTER_BUFFERS: ClassVar[int]
    GL_MAX_TESS_EVALUATION_IMAGE_UNIFORMS: ClassVar[int]
    GL_MAX_TESS_EVALUATION_INPUT_COMPONENTS: ClassVar[int]
    GL_MAX_TESS_EVALUATION_OUTPUT_COMPONENTS: ClassVar[int]
    GL_MAX_TESS_EVALUATION_SHADER_STORAGE_BLOCKS: ClassVar[int]
    GL_MAX_TESS_EVALUATION_TEXTURE_IMAGE_UNITS: ClassVar[int]
    GL_MAX_TESS_EVALUATION_UNIFORM_BLOCKS: ClassVar[int]
    GL_MAX_TESS_EVALUATION_UNIFORM_COMPONENTS: ClassVar[int]
    GL_MAX_TESS_GEN_LEVEL: ClassVar[int]
    GL_MAX_TESS_PATCH_COMPONENTS: ClassVar[int]
    GL_MAX_TEXTURE_BUFFER_SIZE: ClassVar[int]
    GL_MIN_FRAGMENT_INTERPOLATION_OFFSET: ClassVar[int]
    GL_MIN_SAMPLE_SHADING_VALUE: ClassVar[int]
    GL_MULTIPLY: ClassVar[int]
    GL_MULTISAMPLE_LINE_WIDTH_GRANULARITY: ClassVar[int]
    GL_MULTISAMPLE_LINE_WIDTH_RANGE: ClassVar[int]
    GL_NO_RESET_NOTIFICATION: ClassVar[int]
    GL_OVERLAY: ClassVar[int]
    GL_PATCHES: ClassVar[int]
    GL_PATCH_VERTICES: ClassVar[int]
    GL_PRIMITIVES_GENERATED: ClassVar[int]
    GL_PRIMITIVE_BOUNDING_BOX: ClassVar[int]
    GL_PRIMITIVE_RESTART_FOR_PATCHES_SUPPORTED: ClassVar[int]
    GL_PROGRAM: ClassVar[int]
    GL_PROGRAM_PIPELINE: ClassVar[int]
    GL_QUADS: ClassVar[int]
    GL_QUERY: ClassVar[int]
    GL_REFERENCED_BY_GEOMETRY_SHADER: ClassVar[int]
    GL_REFERENCED_BY_TESS_CONTROL_SHADER: ClassVar[int]
    GL_REFERENCED_BY_TESS_EVALUATION_SHADER: ClassVar[int]
    GL_RESET_NOTIFICATION_STRATEGY: ClassVar[int]
    GL_SAMPLER: ClassVar[int]
    GL_SAMPLER_2D_MULTISAMPLE_ARRAY: ClassVar[int]
    GL_SAMPLER_BUFFER: ClassVar[int]
    GL_SAMPLER_CUBE_MAP_ARRAY: ClassVar[int]
    GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW: ClassVar[int]
    GL_SAMPLE_SHADING: ClassVar[int]
    GL_SCREEN: ClassVar[int]
    GL_SHADER: ClassVar[int]
    GL_SOFTLIGHT: ClassVar[int]
    GL_STACK_OVERFLOW: ClassVar[int]
    GL_STACK_UNDERFLOW: ClassVar[int]
    GL_TESS_CONTROL_OUTPUT_VERTICES: ClassVar[int]
    GL_TESS_CONTROL_SHADER: ClassVar[int]
    GL_TESS_CONTROL_SHADER_BIT: ClassVar[int]
    GL_TESS_EVALUATION_SHADER: ClassVar[int]
    GL_TESS_EVALUATION_SHADER_BIT: ClassVar[int]
    GL_TESS_GEN_MODE: ClassVar[int]
    GL_TESS_GEN_POINT_MODE: ClassVar[int]
    GL_TESS_GEN_SPACING: ClassVar[int]
    GL_TESS_GEN_VERTEX_ORDER: ClassVar[int]
    GL_TEXTURE_2D_MULTISAMPLE_ARRAY: ClassVar[int]
    GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY: ClassVar[int]
    GL_TEXTURE_BINDING_BUFFER: ClassVar[int]
    GL_TEXTURE_BINDING_CUBE_MAP_ARRAY: ClassVar[int]
    GL_TEXTURE_BORDER_COLOR: ClassVar[int]
    GL_TEXTURE_BUFFER: ClassVar[int]
    GL_TEXTURE_BUFFER_BINDING: ClassVar[int]
    GL_TEXTURE_BUFFER_DATA_STORE_BINDING: ClassVar[int]
    GL_TEXTURE_BUFFER_OFFSET: ClassVar[int]
    GL_TEXTURE_BUFFER_OFFSET_ALIGNMENT: ClassVar[int]
    GL_TEXTURE_BUFFER_SIZE: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_ARRAY: ClassVar[int]
    GL_TRIANGLES_ADJACENCY: ClassVar[int]
    GL_TRIANGLE_STRIP_ADJACENCY: ClassVar[int]
    GL_UNDEFINED_VERTEX: ClassVar[int]
    GL_UNKNOWN_CONTEXT_RESET: ClassVar[int]
    GL_UNSIGNED_INT_IMAGE_BUFFER: ClassVar[int]
    GL_UNSIGNED_INT_IMAGE_CUBE_MAP_ARRAY: ClassVar[int]
    GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE_ARRAY: ClassVar[int]
    GL_UNSIGNED_INT_SAMPLER_BUFFER: ClassVar[int]
    GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY: ClassVar[int]
    GL_VERTEX_ARRAY: ClassVar[int]
    GL_ACTIVE_ATOMIC_COUNTER_BUFFERS: ClassVar[int]
    GL_ACTIVE_PROGRAM: ClassVar[int]
    GL_ACTIVE_RESOURCES: ClassVar[int]
    GL_ACTIVE_VARIABLES: ClassVar[int]
    GL_ALL_BARRIER_BITS: ClassVar[int]
    GL_ALL_SHADER_BITS: ClassVar[int]
    GL_ARRAY_SIZE: ClassVar[int]
    GL_ARRAY_STRIDE: ClassVar[int]
    GL_ATOMIC_COUNTER_BARRIER_BIT: ClassVar[int]
    GL_ATOMIC_COUNTER_BUFFER: ClassVar[int]
    GL_ATOMIC_COUNTER_BUFFER_BINDING: ClassVar[int]
    GL_ATOMIC_COUNTER_BUFFER_INDEX: ClassVar[int]
    GL_ATOMIC_COUNTER_BUFFER_SIZE: ClassVar[int]
    GL_ATOMIC_COUNTER_BUFFER_START: ClassVar[int]
    GL_BLOCK_INDEX: ClassVar[int]
    GL_BUFFER_BINDING: ClassVar[int]
    GL_BUFFER_DATA_SIZE: ClassVar[int]
    GL_BUFFER_UPDATE_BARRIER_BIT: ClassVar[int]
    GL_BUFFER_VARIABLE: ClassVar[int]
    GL_COMMAND_BARRIER_BIT: ClassVar[int]
    GL_COMPUTE_SHADER: ClassVar[int]
    GL_COMPUTE_SHADER_BIT: ClassVar[int]
    GL_COMPUTE_WORK_GROUP_SIZE: ClassVar[int]
    GL_DEPTH_STENCIL_TEXTURE_MODE: ClassVar[int]
    GL_DISPATCH_INDIRECT_BUFFER: ClassVar[int]
    GL_DISPATCH_INDIRECT_BUFFER_BINDING: ClassVar[int]
    GL_DRAW_INDIRECT_BUFFER: ClassVar[int]
    GL_DRAW_INDIRECT_BUFFER_BINDING: ClassVar[int]
    GL_ELEMENT_ARRAY_BARRIER_BIT: ClassVar[int]
    GL_FRAGMENT_SHADER_BIT: ClassVar[int]
    GL_FRAMEBUFFER_BARRIER_BIT: ClassVar[int]
    GL_FRAMEBUFFER_DEFAULT_FIXED_SAMPLE_LOCATIONS: ClassVar[int]
    GL_FRAMEBUFFER_DEFAULT_HEIGHT: ClassVar[int]
    GL_FRAMEBUFFER_DEFAULT_SAMPLES: ClassVar[int]
    GL_FRAMEBUFFER_DEFAULT_WIDTH: ClassVar[int]
    GL_IMAGE_2D: ClassVar[int]
    GL_IMAGE_2D_ARRAY: ClassVar[int]
    GL_IMAGE_3D: ClassVar[int]
    GL_IMAGE_BINDING_ACCESS: ClassVar[int]
    GL_IMAGE_BINDING_FORMAT: ClassVar[int]
    GL_IMAGE_BINDING_LAYER: ClassVar[int]
    GL_IMAGE_BINDING_LAYERED: ClassVar[int]
    GL_IMAGE_BINDING_LEVEL: ClassVar[int]
    GL_IMAGE_BINDING_NAME: ClassVar[int]
    GL_IMAGE_CUBE: ClassVar[int]
    GL_IMAGE_FORMAT_COMPATIBILITY_BY_CLASS: ClassVar[int]
    GL_IMAGE_FORMAT_COMPATIBILITY_BY_SIZE: ClassVar[int]
    GL_IMAGE_FORMAT_COMPATIBILITY_TYPE: ClassVar[int]
    GL_INT_IMAGE_2D: ClassVar[int]
    GL_INT_IMAGE_2D_ARRAY: ClassVar[int]
    GL_INT_IMAGE_3D: ClassVar[int]
    GL_INT_IMAGE_CUBE: ClassVar[int]
    GL_INT_SAMPLER_2D_MULTISAMPLE: ClassVar[int]
    GL_IS_ROW_MAJOR: ClassVar[int]
    GL_LOCATION: ClassVar[int]
    GL_MATRIX_STRIDE: ClassVar[int]
    GL_MAX_ATOMIC_COUNTER_BUFFER_BINDINGS: ClassVar[int]
    GL_MAX_ATOMIC_COUNTER_BUFFER_SIZE: ClassVar[int]
    GL_MAX_COLOR_TEXTURE_SAMPLES: ClassVar[int]
    GL_MAX_COMBINED_ATOMIC_COUNTERS: ClassVar[int]
    GL_MAX_COMBINED_ATOMIC_COUNTER_BUFFERS: ClassVar[int]
    GL_MAX_COMBINED_COMPUTE_UNIFORM_COMPONENTS: ClassVar[int]
    GL_MAX_COMBINED_IMAGE_UNIFORMS: ClassVar[int]
    GL_MAX_COMBINED_SHADER_OUTPUT_RESOURCES: ClassVar[int]
    GL_MAX_COMBINED_SHADER_STORAGE_BLOCKS: ClassVar[int]
    GL_MAX_COMPUTE_ATOMIC_COUNTERS: ClassVar[int]
    GL_MAX_COMPUTE_ATOMIC_COUNTER_BUFFERS: ClassVar[int]
    GL_MAX_COMPUTE_IMAGE_UNIFORMS: ClassVar[int]
    GL_MAX_COMPUTE_SHADER_STORAGE_BLOCKS: ClassVar[int]
    GL_MAX_COMPUTE_SHARED_MEMORY_SIZE: ClassVar[int]
    GL_MAX_COMPUTE_TEXTURE_IMAGE_UNITS: ClassVar[int]
    GL_MAX_COMPUTE_UNIFORM_BLOCKS: ClassVar[int]
    GL_MAX_COMPUTE_UNIFORM_COMPONENTS: ClassVar[int]
    GL_MAX_COMPUTE_WORK_GROUP_COUNT: ClassVar[int]
    GL_MAX_COMPUTE_WORK_GROUP_INVOCATIONS: ClassVar[int]
    GL_MAX_COMPUTE_WORK_GROUP_SIZE: ClassVar[int]
    GL_MAX_DEPTH_TEXTURE_SAMPLES: ClassVar[int]
    GL_MAX_FRAGMENT_ATOMIC_COUNTERS: ClassVar[int]
    GL_MAX_FRAGMENT_ATOMIC_COUNTER_BUFFERS: ClassVar[int]
    GL_MAX_FRAGMENT_IMAGE_UNIFORMS: ClassVar[int]
    GL_MAX_FRAGMENT_SHADER_STORAGE_BLOCKS: ClassVar[int]
    GL_MAX_FRAMEBUFFER_HEIGHT: ClassVar[int]
    GL_MAX_FRAMEBUFFER_SAMPLES: ClassVar[int]
    GL_MAX_FRAMEBUFFER_WIDTH: ClassVar[int]
    GL_MAX_IMAGE_UNITS: ClassVar[int]
    GL_MAX_INTEGER_SAMPLES: ClassVar[int]
    GL_MAX_NAME_LENGTH: ClassVar[int]
    GL_MAX_NUM_ACTIVE_VARIABLES: ClassVar[int]
    GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET: ClassVar[int]
    GL_MAX_SAMPLE_MASK_WORDS: ClassVar[int]
    GL_MAX_SHADER_STORAGE_BLOCK_SIZE: ClassVar[int]
    GL_MAX_SHADER_STORAGE_BUFFER_BINDINGS: ClassVar[int]
    GL_MAX_UNIFORM_LOCATIONS: ClassVar[int]
    GL_MAX_VERTEX_ATOMIC_COUNTERS: ClassVar[int]
    GL_MAX_VERTEX_ATOMIC_COUNTER_BUFFERS: ClassVar[int]
    GL_MAX_VERTEX_ATTRIB_BINDINGS: ClassVar[int]
    GL_MAX_VERTEX_ATTRIB_RELATIVE_OFFSET: ClassVar[int]
    GL_MAX_VERTEX_ATTRIB_STRIDE: ClassVar[int]
    GL_MAX_VERTEX_IMAGE_UNIFORMS: ClassVar[int]
    GL_MAX_VERTEX_SHADER_STORAGE_BLOCKS: ClassVar[int]
    GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET: ClassVar[int]
    GL_NAME_LENGTH: ClassVar[int]
    GL_NUM_ACTIVE_VARIABLES: ClassVar[int]
    GL_OFFSET: ClassVar[int]
    GL_PIXEL_BUFFER_BARRIER_BIT: ClassVar[int]
    GL_PROGRAM_INPUT: ClassVar[int]
    GL_PROGRAM_OUTPUT: ClassVar[int]
    GL_PROGRAM_PIPELINE_BINDING: ClassVar[int]
    GL_PROGRAM_SEPARABLE: ClassVar[int]
    GL_READ_ONLY: ClassVar[int]
    GL_READ_WRITE: ClassVar[int]
    GL_REFERENCED_BY_COMPUTE_SHADER: ClassVar[int]
    GL_REFERENCED_BY_FRAGMENT_SHADER: ClassVar[int]
    GL_REFERENCED_BY_VERTEX_SHADER: ClassVar[int]
    GL_SAMPLER_2D_MULTISAMPLE: ClassVar[int]
    GL_SAMPLE_MASK: ClassVar[int]
    GL_SAMPLE_MASK_VALUE: ClassVar[int]
    GL_SAMPLE_POSITION: ClassVar[int]
    GL_SHADER_IMAGE_ACCESS_BARRIER_BIT: ClassVar[int]
    GL_SHADER_STORAGE_BARRIER_BIT: ClassVar[int]
    GL_SHADER_STORAGE_BLOCK: ClassVar[int]
    GL_SHADER_STORAGE_BUFFER: ClassVar[int]
    GL_SHADER_STORAGE_BUFFER_BINDING: ClassVar[int]
    GL_SHADER_STORAGE_BUFFER_OFFSET_ALIGNMENT: ClassVar[int]
    GL_SHADER_STORAGE_BUFFER_SIZE: ClassVar[int]
    GL_SHADER_STORAGE_BUFFER_START: ClassVar[int]
    GL_STENCIL_INDEX: ClassVar[int]
    GL_TEXTURE_2D_MULTISAMPLE: ClassVar[int]
    GL_TEXTURE_ALPHA_SIZE: ClassVar[int]
    GL_TEXTURE_ALPHA_TYPE: ClassVar[int]
    GL_TEXTURE_BINDING_2D_MULTISAMPLE: ClassVar[int]
    GL_TEXTURE_BLUE_SIZE: ClassVar[int]
    GL_TEXTURE_BLUE_TYPE: ClassVar[int]
    GL_TEXTURE_COMPRESSED: ClassVar[int]
    GL_TEXTURE_DEPTH: ClassVar[int]
    GL_TEXTURE_DEPTH_SIZE: ClassVar[int]
    GL_TEXTURE_DEPTH_TYPE: ClassVar[int]
    GL_TEXTURE_FETCH_BARRIER_BIT: ClassVar[int]
    GL_TEXTURE_FIXED_SAMPLE_LOCATIONS: ClassVar[int]
    GL_TEXTURE_GREEN_SIZE: ClassVar[int]
    GL_TEXTURE_GREEN_TYPE: ClassVar[int]
    GL_TEXTURE_HEIGHT: ClassVar[int]
    GL_TEXTURE_INTERNAL_FORMAT: ClassVar[int]
    GL_TEXTURE_RED_SIZE: ClassVar[int]
    GL_TEXTURE_RED_TYPE: ClassVar[int]
    GL_TEXTURE_SAMPLES: ClassVar[int]
    GL_TEXTURE_SHARED_SIZE: ClassVar[int]
    GL_TEXTURE_STENCIL_SIZE: ClassVar[int]
    GL_TEXTURE_UPDATE_BARRIER_BIT: ClassVar[int]
    GL_TEXTURE_WIDTH: ClassVar[int]
    GL_TOP_LEVEL_ARRAY_SIZE: ClassVar[int]
    GL_TOP_LEVEL_ARRAY_STRIDE: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_BARRIER_BIT: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_VARYING: ClassVar[int]
    GL_TYPE: ClassVar[int]
    GL_UNIFORM: ClassVar[int]
    GL_UNIFORM_BARRIER_BIT: ClassVar[int]
    GL_UNIFORM_BLOCK: ClassVar[int]
    GL_UNSIGNED_INT_ATOMIC_COUNTER: ClassVar[int]
    GL_UNSIGNED_INT_IMAGE_2D: ClassVar[int]
    GL_UNSIGNED_INT_IMAGE_2D_ARRAY: ClassVar[int]
    GL_UNSIGNED_INT_IMAGE_3D: ClassVar[int]
    GL_UNSIGNED_INT_IMAGE_CUBE: ClassVar[int]
    GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_BARRIER_BIT: ClassVar[int]
    GL_VERTEX_ATTRIB_BINDING: ClassVar[int]
    GL_VERTEX_ATTRIB_RELATIVE_OFFSET: ClassVar[int]
    GL_VERTEX_BINDING_BUFFER: ClassVar[int]
    GL_VERTEX_BINDING_DIVISOR: ClassVar[int]
    GL_VERTEX_BINDING_OFFSET: ClassVar[int]
    GL_VERTEX_BINDING_STRIDE: ClassVar[int]
    GL_VERTEX_SHADER_BIT: ClassVar[int]
    GL_WRITE_ONLY: ClassVar[int]
    GL_ACTIVE_UNIFORM_BLOCKS: ClassVar[int]
    GL_ACTIVE_UNIFORM_BLOCK_MAX_NAME_LENGTH: ClassVar[int]
    GL_ALREADY_SIGNALED: ClassVar[int]
    GL_ANY_SAMPLES_PASSED: ClassVar[int]
    GL_ANY_SAMPLES_PASSED_CONSERVATIVE: ClassVar[int]
    GL_BLUE: ClassVar[int]
    GL_BUFFER_ACCESS_FLAGS: ClassVar[int]
    GL_BUFFER_MAPPED: ClassVar[int]
    GL_BUFFER_MAP_LENGTH: ClassVar[int]
    GL_BUFFER_MAP_OFFSET: ClassVar[int]
    GL_BUFFER_MAP_POINTER: ClassVar[int]
    GL_COLOR: ClassVar[int]
    GL_COLOR_ATTACHMENT1: ClassVar[int]
    GL_COLOR_ATTACHMENT10: ClassVar[int]
    GL_COLOR_ATTACHMENT11: ClassVar[int]
    GL_COLOR_ATTACHMENT12: ClassVar[int]
    GL_COLOR_ATTACHMENT13: ClassVar[int]
    GL_COLOR_ATTACHMENT14: ClassVar[int]
    GL_COLOR_ATTACHMENT15: ClassVar[int]
    GL_COLOR_ATTACHMENT2: ClassVar[int]
    GL_COLOR_ATTACHMENT3: ClassVar[int]
    GL_COLOR_ATTACHMENT4: ClassVar[int]
    GL_COLOR_ATTACHMENT5: ClassVar[int]
    GL_COLOR_ATTACHMENT6: ClassVar[int]
    GL_COLOR_ATTACHMENT7: ClassVar[int]
    GL_COLOR_ATTACHMENT8: ClassVar[int]
    GL_COLOR_ATTACHMENT9: ClassVar[int]
    GL_COMPARE_REF_TO_TEXTURE: ClassVar[int]
    GL_COMPRESSED_R11_EAC: ClassVar[int]
    GL_COMPRESSED_RG11_EAC: ClassVar[int]
    GL_COMPRESSED_RGB8_ETC2: ClassVar[int]
    GL_COMPRESSED_RGB8_PUNCHTHROUGH_ALPHA1_ETC2: ClassVar[int]
    GL_COMPRESSED_RGBA8_ETC2_EAC: ClassVar[int]
    GL_COMPRESSED_SIGNED_R11_EAC: ClassVar[int]
    GL_COMPRESSED_SIGNED_RG11_EAC: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ETC2_EAC: ClassVar[int]
    GL_COMPRESSED_SRGB8_ETC2: ClassVar[int]
    GL_COMPRESSED_SRGB8_PUNCHTHROUGH_ALPHA1_ETC2: ClassVar[int]
    GL_CONDITION_SATISFIED: ClassVar[int]
    GL_COPY_READ_BUFFER: ClassVar[int]
    GL_COPY_READ_BUFFER_BINDING: ClassVar[int]
    GL_COPY_WRITE_BUFFER: ClassVar[int]
    GL_COPY_WRITE_BUFFER_BINDING: ClassVar[int]
    GL_CURRENT_QUERY: ClassVar[int]
    GL_DEPTH: ClassVar[int]
    GL_DEPTH24_STENCIL8: ClassVar[int]
    GL_DEPTH32F_STENCIL8: ClassVar[int]
    GL_DEPTH_COMPONENT24: ClassVar[int]
    GL_DEPTH_COMPONENT32F: ClassVar[int]
    GL_DEPTH_STENCIL: ClassVar[int]
    GL_DEPTH_STENCIL_ATTACHMENT: ClassVar[int]
    GL_DRAW_BUFFER0: ClassVar[int]
    GL_DRAW_BUFFER1: ClassVar[int]
    GL_DRAW_BUFFER10: ClassVar[int]
    GL_DRAW_BUFFER11: ClassVar[int]
    GL_DRAW_BUFFER12: ClassVar[int]
    GL_DRAW_BUFFER13: ClassVar[int]
    GL_DRAW_BUFFER14: ClassVar[int]
    GL_DRAW_BUFFER15: ClassVar[int]
    GL_DRAW_BUFFER2: ClassVar[int]
    GL_DRAW_BUFFER3: ClassVar[int]
    GL_DRAW_BUFFER4: ClassVar[int]
    GL_DRAW_BUFFER5: ClassVar[int]
    GL_DRAW_BUFFER6: ClassVar[int]
    GL_DRAW_BUFFER7: ClassVar[int]
    GL_DRAW_BUFFER8: ClassVar[int]
    GL_DRAW_BUFFER9: ClassVar[int]
    GL_DRAW_FRAMEBUFFER: ClassVar[int]
    GL_DRAW_FRAMEBUFFER_BINDING: ClassVar[int]
    GL_DYNAMIC_COPY: ClassVar[int]
    GL_DYNAMIC_READ: ClassVar[int]
    GL_FLOAT_32_UNSIGNED_INT_24_8_REV: ClassVar[int]
    GL_FLOAT_MAT2x3: ClassVar[int]
    GL_FLOAT_MAT2x4: ClassVar[int]
    GL_FLOAT_MAT3x2: ClassVar[int]
    GL_FLOAT_MAT3x4: ClassVar[int]
    GL_FLOAT_MAT4x2: ClassVar[int]
    GL_FLOAT_MAT4x3: ClassVar[int]
    GL_FRAGMENT_SHADER_DERIVATIVE_HINT: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_ALPHA_SIZE: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_BLUE_SIZE: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_DEPTH_SIZE: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_GREEN_SIZE: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_RED_SIZE: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_STENCIL_SIZE: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER: ClassVar[int]
    GL_FRAMEBUFFER_DEFAULT: ClassVar[int]
    GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE: ClassVar[int]
    GL_FRAMEBUFFER_UNDEFINED: ClassVar[int]
    GL_GREEN: ClassVar[int]
    GL_HALF_FLOAT: ClassVar[int]
    GL_INTERLEAVED_ATTRIBS: ClassVar[int]
    GL_INT_2_10_10_10_REV: ClassVar[int]
    GL_INT_SAMPLER_2D: ClassVar[int]
    GL_INT_SAMPLER_2D_ARRAY: ClassVar[int]
    GL_INT_SAMPLER_3D: ClassVar[int]
    GL_INT_SAMPLER_CUBE: ClassVar[int]
    GL_INVALID_INDEX: ClassVar[int]
    GL_MAJOR_VERSION: ClassVar[int]
    GL_MAP_FLUSH_EXPLICIT_BIT: ClassVar[int]
    GL_MAP_INVALIDATE_BUFFER_BIT: ClassVar[int]
    GL_MAP_INVALIDATE_RANGE_BIT: ClassVar[int]
    GL_MAP_READ_BIT: ClassVar[int]
    GL_MAP_UNSYNCHRONIZED_BIT: ClassVar[int]
    GL_MAP_WRITE_BIT: ClassVar[int]
    GL_MAX: ClassVar[int]
    GL_MAX_3D_TEXTURE_SIZE: ClassVar[int]
    GL_MAX_ARRAY_TEXTURE_LAYERS: ClassVar[int]
    GL_MAX_COLOR_ATTACHMENTS: ClassVar[int]
    GL_MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS: ClassVar[int]
    GL_MAX_COMBINED_UNIFORM_BLOCKS: ClassVar[int]
    GL_MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS: ClassVar[int]
    GL_MAX_DRAW_BUFFERS: ClassVar[int]
    GL_MAX_ELEMENTS_INDICES: ClassVar[int]
    GL_MAX_ELEMENTS_VERTICES: ClassVar[int]
    GL_MAX_ELEMENT_INDEX: ClassVar[int]
    GL_MAX_FRAGMENT_INPUT_COMPONENTS: ClassVar[int]
    GL_MAX_FRAGMENT_UNIFORM_BLOCKS: ClassVar[int]
    GL_MAX_FRAGMENT_UNIFORM_COMPONENTS: ClassVar[int]
    GL_MAX_PROGRAM_TEXEL_OFFSET: ClassVar[int]
    GL_MAX_SAMPLES: ClassVar[int]
    GL_MAX_SERVER_WAIT_TIMEOUT: ClassVar[int]
    GL_MAX_TEXTURE_LOD_BIAS: ClassVar[int]
    GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS: ClassVar[int]
    GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS: ClassVar[int]
    GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS: ClassVar[int]
    GL_MAX_UNIFORM_BLOCK_SIZE: ClassVar[int]
    GL_MAX_UNIFORM_BUFFER_BINDINGS: ClassVar[int]
    GL_MAX_VARYING_COMPONENTS: ClassVar[int]
    GL_MAX_VERTEX_OUTPUT_COMPONENTS: ClassVar[int]
    GL_MAX_VERTEX_UNIFORM_BLOCKS: ClassVar[int]
    GL_MAX_VERTEX_UNIFORM_COMPONENTS: ClassVar[int]
    GL_MIN: ClassVar[int]
    GL_MINOR_VERSION: ClassVar[int]
    GL_MIN_PROGRAM_TEXEL_OFFSET: ClassVar[int]
    GL_NUM_EXTENSIONS: ClassVar[int]
    GL_NUM_PROGRAM_BINARY_FORMATS: ClassVar[int]
    GL_NUM_SAMPLE_COUNTS: ClassVar[int]
    GL_OBJECT_TYPE: ClassVar[int]
    GL_PACK_ROW_LENGTH: ClassVar[int]
    GL_PACK_SKIP_PIXELS: ClassVar[int]
    GL_PACK_SKIP_ROWS: ClassVar[int]
    GL_PIXEL_PACK_BUFFER: ClassVar[int]
    GL_PIXEL_PACK_BUFFER_BINDING: ClassVar[int]
    GL_PIXEL_UNPACK_BUFFER: ClassVar[int]
    GL_PIXEL_UNPACK_BUFFER_BINDING: ClassVar[int]
    GL_PRIMITIVE_RESTART_FIXED_INDEX: ClassVar[int]
    GL_PROGRAM_BINARY_FORMATS: ClassVar[int]
    GL_PROGRAM_BINARY_LENGTH: ClassVar[int]
    GL_PROGRAM_BINARY_RETRIEVABLE_HINT: ClassVar[int]
    GL_QUERY_RESULT: ClassVar[int]
    GL_QUERY_RESULT_AVAILABLE: ClassVar[int]
    GL_R11F_G11F_B10F: ClassVar[int]
    GL_R16F: ClassVar[int]
    GL_R16I: ClassVar[int]
    GL_R16UI: ClassVar[int]
    GL_R32F: ClassVar[int]
    GL_R32I: ClassVar[int]
    GL_R32UI: ClassVar[int]
    GL_R8: ClassVar[int]
    GL_R8I: ClassVar[int]
    GL_R8UI: ClassVar[int]
    GL_R8_SNORM: ClassVar[int]
    GL_RASTERIZER_DISCARD: ClassVar[int]
    GL_READ_BUFFER: ClassVar[int]
    GL_READ_FRAMEBUFFER: ClassVar[int]
    GL_READ_FRAMEBUFFER_BINDING: ClassVar[int]
    GL_RED: ClassVar[int]
    GL_RED_INTEGER: ClassVar[int]
    GL_RENDERBUFFER_SAMPLES: ClassVar[int]
    GL_RG: ClassVar[int]
    GL_RG16F: ClassVar[int]
    GL_RG16I: ClassVar[int]
    GL_RG16UI: ClassVar[int]
    GL_RG32F: ClassVar[int]
    GL_RG32I: ClassVar[int]
    GL_RG32UI: ClassVar[int]
    GL_RG8: ClassVar[int]
    GL_RG8I: ClassVar[int]
    GL_RG8UI: ClassVar[int]
    GL_RG8_SNORM: ClassVar[int]
    GL_RGB10_A2: ClassVar[int]
    GL_RGB10_A2UI: ClassVar[int]
    GL_RGB16F: ClassVar[int]
    GL_RGB16I: ClassVar[int]
    GL_RGB16UI: ClassVar[int]
    GL_RGB32F: ClassVar[int]
    GL_RGB32I: ClassVar[int]
    GL_RGB32UI: ClassVar[int]
    GL_RGB8: ClassVar[int]
    GL_RGB8I: ClassVar[int]
    GL_RGB8UI: ClassVar[int]
    GL_RGB8_SNORM: ClassVar[int]
    GL_RGB9_E5: ClassVar[int]
    GL_RGBA16F: ClassVar[int]
    GL_RGBA16I: ClassVar[int]
    GL_RGBA16UI: ClassVar[int]
    GL_RGBA32F: ClassVar[int]
    GL_RGBA32I: ClassVar[int]
    GL_RGBA32UI: ClassVar[int]
    GL_RGBA8: ClassVar[int]
    GL_RGBA8I: ClassVar[int]
    GL_RGBA8UI: ClassVar[int]
    GL_RGBA8_SNORM: ClassVar[int]
    GL_RGBA_INTEGER: ClassVar[int]
    GL_RGB_INTEGER: ClassVar[int]
    GL_RG_INTEGER: ClassVar[int]
    GL_SAMPLER_2D_ARRAY: ClassVar[int]
    GL_SAMPLER_2D_ARRAY_SHADOW: ClassVar[int]
    GL_SAMPLER_2D_SHADOW: ClassVar[int]
    GL_SAMPLER_3D: ClassVar[int]
    GL_SAMPLER_BINDING: ClassVar[int]
    GL_SAMPLER_CUBE_SHADOW: ClassVar[int]
    GL_SEPARATE_ATTRIBS: ClassVar[int]
    GL_SIGNALED: ClassVar[int]
    GL_SIGNED_NORMALIZED: ClassVar[int]
    GL_SRGB: ClassVar[int]
    GL_SRGB8: ClassVar[int]
    GL_SRGB8_ALPHA8: ClassVar[int]
    GL_STATIC_COPY: ClassVar[int]
    GL_STATIC_READ: ClassVar[int]
    GL_STENCIL: ClassVar[int]
    GL_STREAM_COPY: ClassVar[int]
    GL_STREAM_READ: ClassVar[int]
    GL_SYNC_CONDITION: ClassVar[int]
    GL_SYNC_FENCE: ClassVar[int]
    GL_SYNC_FLAGS: ClassVar[int]
    GL_SYNC_FLUSH_COMMANDS_BIT: ClassVar[int]
    GL_SYNC_GPU_COMMANDS_COMPLETE: ClassVar[int]
    GL_SYNC_STATUS: ClassVar[int]
    GL_TEXTURE_2D_ARRAY: ClassVar[int]
    GL_TEXTURE_3D: ClassVar[int]
    GL_TEXTURE_BASE_LEVEL: ClassVar[int]
    GL_TEXTURE_BINDING_2D_ARRAY: ClassVar[int]
    GL_TEXTURE_BINDING_3D: ClassVar[int]
    GL_TEXTURE_COMPARE_FUNC: ClassVar[int]
    GL_TEXTURE_COMPARE_MODE: ClassVar[int]
    GL_TEXTURE_IMMUTABLE_FORMAT: ClassVar[int]
    GL_TEXTURE_IMMUTABLE_LEVELS: ClassVar[int]
    GL_TEXTURE_MAX_LEVEL: ClassVar[int]
    GL_TEXTURE_MAX_LOD: ClassVar[int]
    GL_TEXTURE_MIN_LOD: ClassVar[int]
    GL_TEXTURE_SWIZZLE_A: ClassVar[int]
    GL_TEXTURE_SWIZZLE_B: ClassVar[int]
    GL_TEXTURE_SWIZZLE_G: ClassVar[int]
    GL_TEXTURE_SWIZZLE_R: ClassVar[int]
    GL_TEXTURE_WRAP_R: ClassVar[int]
    GL_TIMEOUT_EXPIRED: ClassVar[int]
    GL_TIMEOUT_IGNORED: ClassVar[int]
    GL_TRANSFORM_FEEDBACK: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_ACTIVE: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_BINDING: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_BUFFER: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_BUFFER_BINDING: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_BUFFER_MODE: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_BUFFER_SIZE: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_BUFFER_START: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_PAUSED: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_VARYINGS: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH: ClassVar[int]
    GL_UNIFORM_ARRAY_STRIDE: ClassVar[int]
    GL_UNIFORM_BLOCK_ACTIVE_UNIFORMS: ClassVar[int]
    GL_UNIFORM_BLOCK_ACTIVE_UNIFORM_INDICES: ClassVar[int]
    GL_UNIFORM_BLOCK_BINDING: ClassVar[int]
    GL_UNIFORM_BLOCK_DATA_SIZE: ClassVar[int]
    GL_UNIFORM_BLOCK_INDEX: ClassVar[int]
    GL_UNIFORM_BLOCK_NAME_LENGTH: ClassVar[int]
    GL_UNIFORM_BLOCK_REFERENCED_BY_FRAGMENT_SHADER: ClassVar[int]
    GL_UNIFORM_BLOCK_REFERENCED_BY_VERTEX_SHADER: ClassVar[int]
    GL_UNIFORM_BUFFER: ClassVar[int]
    GL_UNIFORM_BUFFER_BINDING: ClassVar[int]
    GL_UNIFORM_BUFFER_OFFSET_ALIGNMENT: ClassVar[int]
    GL_UNIFORM_BUFFER_SIZE: ClassVar[int]
    GL_UNIFORM_BUFFER_START: ClassVar[int]
    GL_UNIFORM_IS_ROW_MAJOR: ClassVar[int]
    GL_UNIFORM_MATRIX_STRIDE: ClassVar[int]
    GL_UNIFORM_NAME_LENGTH: ClassVar[int]
    GL_UNIFORM_OFFSET: ClassVar[int]
    GL_UNIFORM_SIZE: ClassVar[int]
    GL_UNIFORM_TYPE: ClassVar[int]
    GL_UNPACK_IMAGE_HEIGHT: ClassVar[int]
    GL_UNPACK_ROW_LENGTH: ClassVar[int]
    GL_UNPACK_SKIP_IMAGES: ClassVar[int]
    GL_UNPACK_SKIP_PIXELS: ClassVar[int]
    GL_UNPACK_SKIP_ROWS: ClassVar[int]
    GL_UNSIGNALED: ClassVar[int]
    GL_UNSIGNED_INT_10F_11F_11F_REV: ClassVar[int]
    GL_UNSIGNED_INT_24_8: ClassVar[int]
    GL_UNSIGNED_INT_2_10_10_10_REV: ClassVar[int]
    GL_UNSIGNED_INT_5_9_9_9_REV: ClassVar[int]
    GL_UNSIGNED_INT_SAMPLER_2D: ClassVar[int]
    GL_UNSIGNED_INT_SAMPLER_2D_ARRAY: ClassVar[int]
    GL_UNSIGNED_INT_SAMPLER_3D: ClassVar[int]
    GL_UNSIGNED_INT_SAMPLER_CUBE: ClassVar[int]
    GL_UNSIGNED_INT_VEC2: ClassVar[int]
    GL_UNSIGNED_INT_VEC3: ClassVar[int]
    GL_UNSIGNED_INT_VEC4: ClassVar[int]
    GL_UNSIGNED_NORMALIZED: ClassVar[int]
    GL_VERTEX_ARRAY_BINDING: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_DIVISOR: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_INTEGER: ClassVar[int]
    GL_WAIT_FAILED: ClassVar[int]
    GL_ACTIVE_ATTRIBUTES: ClassVar[int]
    GL_ACTIVE_ATTRIBUTE_MAX_LENGTH: ClassVar[int]
    GL_ACTIVE_TEXTURE: ClassVar[int]
    GL_ACTIVE_UNIFORMS: ClassVar[int]
    GL_ACTIVE_UNIFORM_MAX_LENGTH: ClassVar[int]
    GL_ALIASED_LINE_WIDTH_RANGE: ClassVar[int]
    GL_ALIASED_POINT_SIZE_RANGE: ClassVar[int]
    GL_ALPHA: ClassVar[int]
    GL_ALPHA_BITS: ClassVar[int]
    GL_ALWAYS: ClassVar[int]
    GL_ARRAY_BUFFER: ClassVar[int]
    GL_ARRAY_BUFFER_BINDING: ClassVar[int]
    GL_ATTACHED_SHADERS: ClassVar[int]
    GL_BACK: ClassVar[int]
    GL_BLEND: ClassVar[int]
    GL_BLEND_COLOR: ClassVar[int]
    GL_BLEND_DST_ALPHA: ClassVar[int]
    GL_BLEND_DST_RGB: ClassVar[int]
    GL_BLEND_EQUATION: ClassVar[int]
    GL_BLEND_EQUATION_ALPHA: ClassVar[int]
    GL_BLEND_EQUATION_RGB: ClassVar[int]
    GL_BLEND_SRC_ALPHA: ClassVar[int]
    GL_BLEND_SRC_RGB: ClassVar[int]
    GL_BLUE_BITS: ClassVar[int]
    GL_BOOL: ClassVar[int]
    GL_BOOL_VEC2: ClassVar[int]
    GL_BOOL_VEC3: ClassVar[int]
    GL_BOOL_VEC4: ClassVar[int]
    GL_BUFFER_SIZE: ClassVar[int]
    GL_BUFFER_USAGE: ClassVar[int]
    GL_BYTE: ClassVar[int]
    GL_CCW: ClassVar[int]
    GL_CLAMP_TO_EDGE: ClassVar[int]
    GL_COLOR_ATTACHMENT0: ClassVar[int]
    GL_COLOR_BUFFER_BIT: ClassVar[int]
    GL_COLOR_CLEAR_VALUE: ClassVar[int]
    GL_COLOR_WRITEMASK: ClassVar[int]
    GL_COMPILE_STATUS: ClassVar[int]
    GL_COMPRESSED_TEXTURE_FORMATS: ClassVar[int]
    GL_CONSTANT_ALPHA: ClassVar[int]
    GL_CONSTANT_COLOR: ClassVar[int]
    GL_CULL_FACE: ClassVar[int]
    GL_CULL_FACE_MODE: ClassVar[int]
    GL_CURRENT_PROGRAM: ClassVar[int]
    GL_CURRENT_VERTEX_ATTRIB: ClassVar[int]
    GL_CW: ClassVar[int]
    GL_DECR: ClassVar[int]
    GL_DECR_WRAP: ClassVar[int]
    GL_DELETE_STATUS: ClassVar[int]
    GL_DEPTH_ATTACHMENT: ClassVar[int]
    GL_DEPTH_BITS: ClassVar[int]
    GL_DEPTH_BUFFER_BIT: ClassVar[int]
    GL_DEPTH_CLEAR_VALUE: ClassVar[int]
    GL_DEPTH_COMPONENT: ClassVar[int]
    GL_DEPTH_COMPONENT16: ClassVar[int]
    GL_DEPTH_FUNC: ClassVar[int]
    GL_DEPTH_RANGE: ClassVar[int]
    GL_DEPTH_TEST: ClassVar[int]
    GL_DEPTH_WRITEMASK: ClassVar[int]
    GL_DITHER: ClassVar[int]
    GL_DONT_CARE: ClassVar[int]
    GL_DST_ALPHA: ClassVar[int]
    GL_DST_COLOR: ClassVar[int]
    GL_DYNAMIC_DRAW: ClassVar[int]
    GL_ELEMENT_ARRAY_BUFFER: ClassVar[int]
    GL_ELEMENT_ARRAY_BUFFER_BINDING: ClassVar[int]
    GL_EQUAL: ClassVar[int]
    GL_EXTENSIONS: ClassVar[int]
    GL_FALSE: ClassVar[int]
    GL_FASTEST: ClassVar[int]
    GL_FIXED: ClassVar[int]
    GL_FLOAT: ClassVar[int]
    GL_FLOAT_MAT2: ClassVar[int]
    GL_FLOAT_MAT3: ClassVar[int]
    GL_FLOAT_MAT4: ClassVar[int]
    GL_FLOAT_VEC2: ClassVar[int]
    GL_FLOAT_VEC3: ClassVar[int]
    GL_FLOAT_VEC4: ClassVar[int]
    GL_FRAGMENT_SHADER: ClassVar[int]
    GL_FRAMEBUFFER: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL: ClassVar[int]
    GL_FRAMEBUFFER_BINDING: ClassVar[int]
    GL_FRAMEBUFFER_COMPLETE: ClassVar[int]
    GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT: ClassVar[int]
    GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS: ClassVar[int]
    GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT: ClassVar[int]
    GL_FRAMEBUFFER_UNSUPPORTED: ClassVar[int]
    GL_FRONT: ClassVar[int]
    GL_FRONT_AND_BACK: ClassVar[int]
    GL_FRONT_FACE: ClassVar[int]
    GL_FUNC_ADD: ClassVar[int]
    GL_FUNC_REVERSE_SUBTRACT: ClassVar[int]
    GL_FUNC_SUBTRACT: ClassVar[int]
    GL_GENERATE_MIPMAP_HINT: ClassVar[int]
    GL_GEQUAL: ClassVar[int]
    GL_GREATER: ClassVar[int]
    GL_GREEN_BITS: ClassVar[int]
    GL_HIGH_FLOAT: ClassVar[int]
    GL_HIGH_INT: ClassVar[int]
    GL_IMPLEMENTATION_COLOR_READ_FORMAT: ClassVar[int]
    GL_IMPLEMENTATION_COLOR_READ_TYPE: ClassVar[int]
    GL_INCR: ClassVar[int]
    GL_INCR_WRAP: ClassVar[int]
    GL_INFO_LOG_LENGTH: ClassVar[int]
    GL_INT: ClassVar[int]
    GL_INT_VEC2: ClassVar[int]
    GL_INT_VEC3: ClassVar[int]
    GL_INT_VEC4: ClassVar[int]
    GL_INVALID_ENUM: ClassVar[int]
    GL_INVALID_FRAMEBUFFER_OPERATION: ClassVar[int]
    GL_INVALID_OPERATION: ClassVar[int]
    GL_INVALID_VALUE: ClassVar[int]
    GL_INVERT: ClassVar[int]
    GL_KEEP: ClassVar[int]
    GL_LEQUAL: ClassVar[int]
    GL_LESS: ClassVar[int]
    GL_LINEAR: ClassVar[int]
    GL_LINEAR_MIPMAP_LINEAR: ClassVar[int]
    GL_LINEAR_MIPMAP_NEAREST: ClassVar[int]
    GL_LINES: ClassVar[int]
    GL_LINE_LOOP: ClassVar[int]
    GL_LINE_STRIP: ClassVar[int]
    GL_LINE_WIDTH: ClassVar[int]
    GL_LINK_STATUS: ClassVar[int]
    GL_LOW_FLOAT: ClassVar[int]
    GL_LOW_INT: ClassVar[int]
    GL_LUMINANCE: ClassVar[int]
    GL_LUMINANCE_ALPHA: ClassVar[int]
    GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS: ClassVar[int]
    GL_MAX_CUBE_MAP_TEXTURE_SIZE: ClassVar[int]
    GL_MAX_FRAGMENT_UNIFORM_VECTORS: ClassVar[int]
    GL_MAX_RENDERBUFFER_SIZE: ClassVar[int]
    GL_MAX_TEXTURE_IMAGE_UNITS: ClassVar[int]
    GL_MAX_TEXTURE_SIZE: ClassVar[int]
    GL_MAX_VARYING_VECTORS: ClassVar[int]
    GL_MAX_VERTEX_ATTRIBS: ClassVar[int]
    GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS: ClassVar[int]
    GL_MAX_VERTEX_UNIFORM_VECTORS: ClassVar[int]
    GL_MAX_VIEWPORT_DIMS: ClassVar[int]
    GL_MEDIUM_FLOAT: ClassVar[int]
    GL_MEDIUM_INT: ClassVar[int]
    GL_MIRRORED_REPEAT: ClassVar[int]
    GL_NEAREST: ClassVar[int]
    GL_NEAREST_MIPMAP_LINEAR: ClassVar[int]
    GL_NEAREST_MIPMAP_NEAREST: ClassVar[int]
    GL_NEVER: ClassVar[int]
    GL_NICEST: ClassVar[int]
    GL_NONE: ClassVar[int]
    GL_NOTEQUAL: ClassVar[int]
    GL_NO_ERROR: ClassVar[int]
    GL_NUM_COMPRESSED_TEXTURE_FORMATS: ClassVar[int]
    GL_NUM_SHADER_BINARY_FORMATS: ClassVar[int]
    GL_ONE: ClassVar[int]
    GL_ONE_MINUS_CONSTANT_ALPHA: ClassVar[int]
    GL_ONE_MINUS_CONSTANT_COLOR: ClassVar[int]
    GL_ONE_MINUS_DST_ALPHA: ClassVar[int]
    GL_ONE_MINUS_DST_COLOR: ClassVar[int]
    GL_ONE_MINUS_SRC_ALPHA: ClassVar[int]
    GL_ONE_MINUS_SRC_COLOR: ClassVar[int]
    GL_OUT_OF_MEMORY: ClassVar[int]
    GL_PACK_ALIGNMENT: ClassVar[int]
    GL_POINTS: ClassVar[int]
    GL_POLYGON_OFFSET_FACTOR: ClassVar[int]
    GL_POLYGON_OFFSET_FILL: ClassVar[int]
    GL_POLYGON_OFFSET_UNITS: ClassVar[int]
    GL_RED_BITS: ClassVar[int]
    GL_RENDERBUFFER: ClassVar[int]
    GL_RENDERBUFFER_ALPHA_SIZE: ClassVar[int]
    GL_RENDERBUFFER_BINDING: ClassVar[int]
    GL_RENDERBUFFER_BLUE_SIZE: ClassVar[int]
    GL_RENDERBUFFER_DEPTH_SIZE: ClassVar[int]
    GL_RENDERBUFFER_GREEN_SIZE: ClassVar[int]
    GL_RENDERBUFFER_HEIGHT: ClassVar[int]
    GL_RENDERBUFFER_INTERNAL_FORMAT: ClassVar[int]
    GL_RENDERBUFFER_RED_SIZE: ClassVar[int]
    GL_RENDERBUFFER_STENCIL_SIZE: ClassVar[int]
    GL_RENDERBUFFER_WIDTH: ClassVar[int]
    GL_RENDERER: ClassVar[int]
    GL_REPEAT: ClassVar[int]
    GL_REPLACE: ClassVar[int]
    GL_RGB: ClassVar[int]
    GL_RGB565: ClassVar[int]
    GL_RGB5_A1: ClassVar[int]
    GL_RGBA: ClassVar[int]
    GL_RGBA4: ClassVar[int]
    GL_SAMPLER_2D: ClassVar[int]
    GL_SAMPLER_CUBE: ClassVar[int]
    GL_SAMPLES: ClassVar[int]
    GL_SAMPLE_ALPHA_TO_COVERAGE: ClassVar[int]
    GL_SAMPLE_BUFFERS: ClassVar[int]
    GL_SAMPLE_COVERAGE: ClassVar[int]
    GL_SAMPLE_COVERAGE_INVERT: ClassVar[int]
    GL_SAMPLE_COVERAGE_VALUE: ClassVar[int]
    GL_SCISSOR_BOX: ClassVar[int]
    GL_SCISSOR_TEST: ClassVar[int]
    GL_SHADER_BINARY_FORMATS: ClassVar[int]
    GL_SHADER_COMPILER: ClassVar[int]
    GL_SHADER_SOURCE_LENGTH: ClassVar[int]
    GL_SHADER_TYPE: ClassVar[int]
    GL_SHADING_LANGUAGE_VERSION: ClassVar[int]
    GL_SHORT: ClassVar[int]
    GL_SRC_ALPHA: ClassVar[int]
    GL_SRC_ALPHA_SATURATE: ClassVar[int]
    GL_SRC_COLOR: ClassVar[int]
    GL_STATIC_DRAW: ClassVar[int]
    GL_STENCIL_ATTACHMENT: ClassVar[int]
    GL_STENCIL_BACK_FAIL: ClassVar[int]
    GL_STENCIL_BACK_FUNC: ClassVar[int]
    GL_STENCIL_BACK_PASS_DEPTH_FAIL: ClassVar[int]
    GL_STENCIL_BACK_PASS_DEPTH_PASS: ClassVar[int]
    GL_STENCIL_BACK_REF: ClassVar[int]
    GL_STENCIL_BACK_VALUE_MASK: ClassVar[int]
    GL_STENCIL_BACK_WRITEMASK: ClassVar[int]
    GL_STENCIL_BITS: ClassVar[int]
    GL_STENCIL_BUFFER_BIT: ClassVar[int]
    GL_STENCIL_CLEAR_VALUE: ClassVar[int]
    GL_STENCIL_FAIL: ClassVar[int]
    GL_STENCIL_FUNC: ClassVar[int]
    GL_STENCIL_INDEX: ClassVar[int]
    GL_STENCIL_INDEX8: ClassVar[int]
    GL_STENCIL_PASS_DEPTH_FAIL: ClassVar[int]
    GL_STENCIL_PASS_DEPTH_PASS: ClassVar[int]
    GL_STENCIL_REF: ClassVar[int]
    GL_STENCIL_TEST: ClassVar[int]
    GL_STENCIL_VALUE_MASK: ClassVar[int]
    GL_STENCIL_WRITEMASK: ClassVar[int]
    GL_STREAM_DRAW: ClassVar[int]
    GL_SUBPIXEL_BITS: ClassVar[int]
    GL_TEXTURE: ClassVar[int]
    GL_TEXTURE0: ClassVar[int]
    GL_TEXTURE1: ClassVar[int]
    GL_TEXTURE10: ClassVar[int]
    GL_TEXTURE11: ClassVar[int]
    GL_TEXTURE12: ClassVar[int]
    GL_TEXTURE13: ClassVar[int]
    GL_TEXTURE14: ClassVar[int]
    GL_TEXTURE15: ClassVar[int]
    GL_TEXTURE16: ClassVar[int]
    GL_TEXTURE17: ClassVar[int]
    GL_TEXTURE18: ClassVar[int]
    GL_TEXTURE19: ClassVar[int]
    GL_TEXTURE2: ClassVar[int]
    GL_TEXTURE20: ClassVar[int]
    GL_TEXTURE21: ClassVar[int]
    GL_TEXTURE22: ClassVar[int]
    GL_TEXTURE23: ClassVar[int]
    GL_TEXTURE24: ClassVar[int]
    GL_TEXTURE25: ClassVar[int]
    GL_TEXTURE26: ClassVar[int]
    GL_TEXTURE27: ClassVar[int]
    GL_TEXTURE28: ClassVar[int]
    GL_TEXTURE29: ClassVar[int]
    GL_TEXTURE3: ClassVar[int]
    GL_TEXTURE30: ClassVar[int]
    GL_TEXTURE31: ClassVar[int]
    GL_TEXTURE4: ClassVar[int]
    GL_TEXTURE5: ClassVar[int]
    GL_TEXTURE6: ClassVar[int]
    GL_TEXTURE7: ClassVar[int]
    GL_TEXTURE8: ClassVar[int]
    GL_TEXTURE9: ClassVar[int]
    GL_TEXTURE_2D: ClassVar[int]
    GL_TEXTURE_BINDING_2D: ClassVar[int]
    GL_TEXTURE_BINDING_CUBE_MAP: ClassVar[int]
    GL_TEXTURE_CUBE_MAP: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_NEGATIVE_X: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_NEGATIVE_Y: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_NEGATIVE_Z: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_POSITIVE_X: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_POSITIVE_Y: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_POSITIVE_Z: ClassVar[int]
    GL_TEXTURE_MAG_FILTER: ClassVar[int]
    GL_TEXTURE_MIN_FILTER: ClassVar[int]
    GL_TEXTURE_WRAP_S: ClassVar[int]
    GL_TEXTURE_WRAP_T: ClassVar[int]
    GL_TRIANGLES: ClassVar[int]
    GL_TRIANGLE_FAN: ClassVar[int]
    GL_TRIANGLE_STRIP: ClassVar[int]
    GL_TRUE: ClassVar[int]
    GL_UNPACK_ALIGNMENT: ClassVar[int]
    GL_UNSIGNED_BYTE: ClassVar[int]
    GL_UNSIGNED_INT: ClassVar[int]
    GL_UNSIGNED_SHORT: ClassVar[int]
    GL_UNSIGNED_SHORT_4_4_4_4: ClassVar[int]
    GL_UNSIGNED_SHORT_5_5_5_1: ClassVar[int]
    GL_UNSIGNED_SHORT_5_6_5: ClassVar[int]
    GL_VALIDATE_STATUS: ClassVar[int]
    GL_VENDOR: ClassVar[int]
    GL_VERSION: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_ENABLED: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_NORMALIZED: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_POINTER: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_SIZE: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_STRIDE: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_TYPE: ClassVar[int]
    GL_VERTEX_SHADER: ClassVar[int]
    GL_VIEWPORT: ClassVar[int]
    GL_ZERO: ClassVar[int]
    @staticmethod
    def glBlendBarrier() -> None: ...
    @staticmethod
    def glBlendEquationSeparatei(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glBlendEquationi(p0: int, p1: int) -> None: ...
    @staticmethod
    def glBlendFuncSeparatei(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @staticmethod
    def glBlendFunci(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glColorMaski(p0: int, p1: bool, p2: bool, p3: bool, p4: bool) -> None: ...
    @staticmethod
    def glCopyImageSubData(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: int, p9: int, p10: int, p11: int, p12: int, p13: int, p14: int) -> None: ...
    @staticmethod
    def glDebugMessageCallback(p0: Any) -> None: ...
    @overload
    @staticmethod
    def glDebugMessageControl(p0: int, p1: int, p2: int, p3: int, p4: Any, p5: int, p6: bool) -> None: ...
    @overload
    @staticmethod
    def glDebugMessageControl(p0: int, p1: int, p2: int, p3: int, p4: IntBuffer, p5: bool) -> None: ...
    @staticmethod
    def glDebugMessageInsert(p0: int, p1: int, p2: int, p3: int, p4: int, p5: str) -> None: ...
    @staticmethod
    def glDisablei(p0: int, p1: int) -> None: ...
    @staticmethod
    def glDrawElementsBaseVertex(p0: int, p1: int, p2: int, p3: Buffer, p4: int) -> None: ...
    @overload
    @staticmethod
    def glDrawElementsInstancedBaseVertex(p0: int, p1: int, p2: int, p3: Buffer, p4: int, p5: int) -> None: ...
    @overload
    @staticmethod
    def glDrawElementsInstancedBaseVertex(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int) -> None: ...
    @staticmethod
    def glDrawRangeElementsBaseVertex(p0: int, p1: int, p2: int, p3: int, p4: int, p5: Buffer, p6: int) -> None: ...
    @staticmethod
    def glEnablei(p0: int, p1: int) -> None: ...
    @staticmethod
    def glFramebufferTexture(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetDebugMessageLog(p0: int, p1: IntBuffer, p2: IntBuffer, p3: IntBuffer, p4: IntBuffer) -> Any: ...
    @overload
    @staticmethod
    def glGetDebugMessageLog(p0: int, p1: IntBuffer, p2: IntBuffer, p3: IntBuffer, p4: IntBuffer, p5: IntBuffer, p6: ByteBuffer) -> int: ...
    @overload
    @staticmethod
    def glGetDebugMessageLog(p0: int, p1: Any, p2: int, p3: Any, p4: int, p5: Any, p6: int, p7: Any, p8: int) -> Any: ...
    @overload
    @staticmethod
    def glGetDebugMessageLog(p0: int, p1: int, p2: Any, p3: int, p4: Any, p5: int, p6: Any, p7: int, p8: Any, p9: int, p10: Any, p11: int, p12: Any, p13: int) -> int: ...
    @staticmethod
    def glGetGraphicsResetStatus() -> int: ...
    @staticmethod
    def glGetObjectLabel(p0: int, p1: int) -> str: ...
    @staticmethod
    def glGetObjectPtrLabel(p0: int) -> str: ...
    @staticmethod
    def glGetPointerv(p0: int) -> int: ...
    @overload
    @staticmethod
    def glGetSamplerParameterIiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetSamplerParameterIiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetSamplerParameterIuiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetSamplerParameterIuiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameterIiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameterIiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameterIuiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameterIuiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetnUniformfv(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glGetnUniformfv(p0: int, p1: int, p2: int, p3: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetnUniformiv(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glGetnUniformiv(p0: int, p1: int, p2: int, p3: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetnUniformuiv(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glGetnUniformuiv(p0: int, p1: int, p2: int, p3: IntBuffer) -> None: ...
    @staticmethod
    def glIsEnabledi(p0: int, p1: int) -> bool: ...
    @staticmethod
    def glMinSampleShading(p0: float) -> None: ...
    @staticmethod
    def glObjectLabel(p0: int, p1: int, p2: int, p3: str) -> None: ...
    @staticmethod
    def glObjectPtrLabel(p0: int, p1: str) -> None: ...
    @staticmethod
    def glPatchParameteri(p0: int, p1: int) -> None: ...
    @staticmethod
    def glPopDebugGroup() -> None: ...
    @staticmethod
    def glPrimitiveBoundingBox(p0: float, p1: float, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float) -> None: ...
    @staticmethod
    def glPushDebugGroup(p0: int, p1: int, p2: int, p3: str) -> None: ...
    @staticmethod
    def glReadnPixels(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: Buffer) -> None: ...
    @overload
    @staticmethod
    def glSamplerParameterIiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glSamplerParameterIiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glSamplerParameterIuiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glSamplerParameterIuiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def glTexBuffer(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glTexBufferRange(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @overload
    @staticmethod
    def glTexParameterIiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glTexParameterIiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glTexParameterIuiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glTexParameterIuiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @staticmethod
    def glTexStorage3DMultisample(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: bool) -> None: ...

    class DebugProc:
        def onMessage(self, p0: int, p1: int, p2: int, p3: int, p4: str) -> None: ...

from typing import Any, ClassVar, overload
from java.nio.IntBuffer import IntBuffer

class GLES10Ext:
    def __init__(self) -> None: ...
    @overload
    @staticmethod
    def glQueryMatrixxOES(p0: Any, p1: int, p2: Any, p3: int) -> int: ...
    @overload
    @staticmethod
    def glQueryMatrixxOES(p0: IntBuffer, p1: IntBuffer) -> int: ...

from typing import Any, ClassVar, overload
from java.nio.Buffer import Buffer
from java.nio.FloatBuffer import FloatBuffer
from java.nio.IntBuffer import IntBuffer

class GLES11:
    GL_ACTIVE_TEXTURE: ClassVar[int]
    GL_ADD_SIGNED: ClassVar[int]
    GL_ALPHA_SCALE: ClassVar[int]
    GL_ALPHA_TEST_FUNC: ClassVar[int]
    GL_ALPHA_TEST_REF: ClassVar[int]
    GL_ARRAY_BUFFER: ClassVar[int]
    GL_ARRAY_BUFFER_BINDING: ClassVar[int]
    GL_BLEND_DST: ClassVar[int]
    GL_BLEND_SRC: ClassVar[int]
    GL_BUFFER_ACCESS: ClassVar[int]
    GL_BUFFER_SIZE: ClassVar[int]
    GL_BUFFER_USAGE: ClassVar[int]
    GL_CLIENT_ACTIVE_TEXTURE: ClassVar[int]
    GL_CLIP_PLANE0: ClassVar[int]
    GL_CLIP_PLANE1: ClassVar[int]
    GL_CLIP_PLANE2: ClassVar[int]
    GL_CLIP_PLANE3: ClassVar[int]
    GL_CLIP_PLANE4: ClassVar[int]
    GL_CLIP_PLANE5: ClassVar[int]
    GL_COLOR_ARRAY_BUFFER_BINDING: ClassVar[int]
    GL_COLOR_ARRAY_POINTER: ClassVar[int]
    GL_COLOR_ARRAY_SIZE: ClassVar[int]
    GL_COLOR_ARRAY_STRIDE: ClassVar[int]
    GL_COLOR_ARRAY_TYPE: ClassVar[int]
    GL_COLOR_CLEAR_VALUE: ClassVar[int]
    GL_COLOR_WRITEMASK: ClassVar[int]
    GL_COMBINE: ClassVar[int]
    GL_COMBINE_ALPHA: ClassVar[int]
    GL_COMBINE_RGB: ClassVar[int]
    GL_CONSTANT: ClassVar[int]
    GL_COORD_REPLACE_OES: ClassVar[int]
    GL_CULL_FACE_MODE: ClassVar[int]
    GL_CURRENT_COLOR: ClassVar[int]
    GL_CURRENT_NORMAL: ClassVar[int]
    GL_CURRENT_TEXTURE_COORDS: ClassVar[int]
    GL_DEPTH_CLEAR_VALUE: ClassVar[int]
    GL_DEPTH_FUNC: ClassVar[int]
    GL_DEPTH_RANGE: ClassVar[int]
    GL_DEPTH_WRITEMASK: ClassVar[int]
    GL_DOT3_RGB: ClassVar[int]
    GL_DOT3_RGBA: ClassVar[int]
    GL_DYNAMIC_DRAW: ClassVar[int]
    GL_ELEMENT_ARRAY_BUFFER: ClassVar[int]
    GL_ELEMENT_ARRAY_BUFFER_BINDING: ClassVar[int]
    GL_FRONT_FACE: ClassVar[int]
    GL_GENERATE_MIPMAP: ClassVar[int]
    GL_GENERATE_MIPMAP_HINT: ClassVar[int]
    GL_INTERPOLATE: ClassVar[int]
    GL_LINE_WIDTH: ClassVar[int]
    GL_LOGIC_OP_MODE: ClassVar[int]
    GL_MATRIX_MODE: ClassVar[int]
    GL_MAX_CLIP_PLANES: ClassVar[int]
    GL_MODELVIEW_MATRIX: ClassVar[int]
    GL_MODELVIEW_MATRIX_FLOAT_AS_INT_BITS_OES: ClassVar[int]
    GL_MODELVIEW_STACK_DEPTH: ClassVar[int]
    GL_NORMAL_ARRAY_BUFFER_BINDING: ClassVar[int]
    GL_NORMAL_ARRAY_POINTER: ClassVar[int]
    GL_NORMAL_ARRAY_STRIDE: ClassVar[int]
    GL_NORMAL_ARRAY_TYPE: ClassVar[int]
    GL_OPERAND0_ALPHA: ClassVar[int]
    GL_OPERAND0_RGB: ClassVar[int]
    GL_OPERAND1_ALPHA: ClassVar[int]
    GL_OPERAND1_RGB: ClassVar[int]
    GL_OPERAND2_ALPHA: ClassVar[int]
    GL_OPERAND2_RGB: ClassVar[int]
    GL_POINT_DISTANCE_ATTENUATION: ClassVar[int]
    GL_POINT_FADE_THRESHOLD_SIZE: ClassVar[int]
    GL_POINT_SIZE: ClassVar[int]
    GL_POINT_SIZE_ARRAY_BUFFER_BINDING_OES: ClassVar[int]
    GL_POINT_SIZE_ARRAY_OES: ClassVar[int]
    GL_POINT_SIZE_ARRAY_POINTER_OES: ClassVar[int]
    GL_POINT_SIZE_ARRAY_STRIDE_OES: ClassVar[int]
    GL_POINT_SIZE_ARRAY_TYPE_OES: ClassVar[int]
    GL_POINT_SIZE_MAX: ClassVar[int]
    GL_POINT_SIZE_MIN: ClassVar[int]
    GL_POINT_SPRITE_OES: ClassVar[int]
    GL_POLYGON_OFFSET_FACTOR: ClassVar[int]
    GL_POLYGON_OFFSET_UNITS: ClassVar[int]
    GL_PREVIOUS: ClassVar[int]
    GL_PRIMARY_COLOR: ClassVar[int]
    GL_PROJECTION_MATRIX: ClassVar[int]
    GL_PROJECTION_MATRIX_FLOAT_AS_INT_BITS_OES: ClassVar[int]
    GL_PROJECTION_STACK_DEPTH: ClassVar[int]
    GL_RGB_SCALE: ClassVar[int]
    GL_SAMPLES: ClassVar[int]
    GL_SAMPLE_BUFFERS: ClassVar[int]
    GL_SAMPLE_COVERAGE_INVERT: ClassVar[int]
    GL_SAMPLE_COVERAGE_VALUE: ClassVar[int]
    GL_SCISSOR_BOX: ClassVar[int]
    GL_SHADE_MODEL: ClassVar[int]
    GL_SRC0_ALPHA: ClassVar[int]
    GL_SRC0_RGB: ClassVar[int]
    GL_SRC1_ALPHA: ClassVar[int]
    GL_SRC1_RGB: ClassVar[int]
    GL_SRC2_ALPHA: ClassVar[int]
    GL_SRC2_RGB: ClassVar[int]
    GL_STATIC_DRAW: ClassVar[int]
    GL_STENCIL_CLEAR_VALUE: ClassVar[int]
    GL_STENCIL_FAIL: ClassVar[int]
    GL_STENCIL_FUNC: ClassVar[int]
    GL_STENCIL_PASS_DEPTH_FAIL: ClassVar[int]
    GL_STENCIL_PASS_DEPTH_PASS: ClassVar[int]
    GL_STENCIL_REF: ClassVar[int]
    GL_STENCIL_VALUE_MASK: ClassVar[int]
    GL_STENCIL_WRITEMASK: ClassVar[int]
    GL_SUBTRACT: ClassVar[int]
    GL_TEXTURE_BINDING_2D: ClassVar[int]
    GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING: ClassVar[int]
    GL_TEXTURE_COORD_ARRAY_POINTER: ClassVar[int]
    GL_TEXTURE_COORD_ARRAY_SIZE: ClassVar[int]
    GL_TEXTURE_COORD_ARRAY_STRIDE: ClassVar[int]
    GL_TEXTURE_COORD_ARRAY_TYPE: ClassVar[int]
    GL_TEXTURE_MATRIX: ClassVar[int]
    GL_TEXTURE_MATRIX_FLOAT_AS_INT_BITS_OES: ClassVar[int]
    GL_TEXTURE_STACK_DEPTH: ClassVar[int]
    GL_VERTEX_ARRAY_BUFFER_BINDING: ClassVar[int]
    GL_VERTEX_ARRAY_POINTER: ClassVar[int]
    GL_VERTEX_ARRAY_SIZE: ClassVar[int]
    GL_VERTEX_ARRAY_STRIDE: ClassVar[int]
    GL_VERTEX_ARRAY_TYPE: ClassVar[int]
    GL_VIEWPORT: ClassVar[int]
    GL_WRITE_ONLY: ClassVar[int]
    GL_ADD: ClassVar[int]
    GL_ALIASED_LINE_WIDTH_RANGE: ClassVar[int]
    GL_ALIASED_POINT_SIZE_RANGE: ClassVar[int]
    GL_ALPHA: ClassVar[int]
    GL_ALPHA_BITS: ClassVar[int]
    GL_ALPHA_TEST: ClassVar[int]
    GL_ALWAYS: ClassVar[int]
    GL_AMBIENT: ClassVar[int]
    GL_AMBIENT_AND_DIFFUSE: ClassVar[int]
    GL_AND: ClassVar[int]
    GL_AND_INVERTED: ClassVar[int]
    GL_AND_REVERSE: ClassVar[int]
    GL_BACK: ClassVar[int]
    GL_BLEND: ClassVar[int]
    GL_BLUE_BITS: ClassVar[int]
    GL_BYTE: ClassVar[int]
    GL_CCW: ClassVar[int]
    GL_CLAMP_TO_EDGE: ClassVar[int]
    GL_CLEAR: ClassVar[int]
    GL_COLOR_ARRAY: ClassVar[int]
    GL_COLOR_BUFFER_BIT: ClassVar[int]
    GL_COLOR_LOGIC_OP: ClassVar[int]
    GL_COLOR_MATERIAL: ClassVar[int]
    GL_COMPRESSED_TEXTURE_FORMATS: ClassVar[int]
    GL_CONSTANT_ATTENUATION: ClassVar[int]
    GL_COPY: ClassVar[int]
    GL_COPY_INVERTED: ClassVar[int]
    GL_CULL_FACE: ClassVar[int]
    GL_CW: ClassVar[int]
    GL_DECAL: ClassVar[int]
    GL_DECR: ClassVar[int]
    GL_DEPTH_BITS: ClassVar[int]
    GL_DEPTH_BUFFER_BIT: ClassVar[int]
    GL_DEPTH_TEST: ClassVar[int]
    GL_DIFFUSE: ClassVar[int]
    GL_DITHER: ClassVar[int]
    GL_DONT_CARE: ClassVar[int]
    GL_DST_ALPHA: ClassVar[int]
    GL_DST_COLOR: ClassVar[int]
    GL_EMISSION: ClassVar[int]
    GL_EQUAL: ClassVar[int]
    GL_EQUIV: ClassVar[int]
    GL_EXP: ClassVar[int]
    GL_EXP2: ClassVar[int]
    GL_EXTENSIONS: ClassVar[int]
    GL_FALSE: ClassVar[int]
    GL_FASTEST: ClassVar[int]
    GL_FIXED: ClassVar[int]
    GL_FLAT: ClassVar[int]
    GL_FLOAT: ClassVar[int]
    GL_FOG: ClassVar[int]
    GL_FOG_COLOR: ClassVar[int]
    GL_FOG_DENSITY: ClassVar[int]
    GL_FOG_END: ClassVar[int]
    GL_FOG_HINT: ClassVar[int]
    GL_FOG_MODE: ClassVar[int]
    GL_FOG_START: ClassVar[int]
    GL_FRONT: ClassVar[int]
    GL_FRONT_AND_BACK: ClassVar[int]
    GL_GEQUAL: ClassVar[int]
    GL_GREATER: ClassVar[int]
    GL_GREEN_BITS: ClassVar[int]
    GL_IMPLEMENTATION_COLOR_READ_FORMAT_OES: ClassVar[int]
    GL_IMPLEMENTATION_COLOR_READ_TYPE_OES: ClassVar[int]
    GL_INCR: ClassVar[int]
    GL_INVALID_ENUM: ClassVar[int]
    GL_INVALID_OPERATION: ClassVar[int]
    GL_INVALID_VALUE: ClassVar[int]
    GL_INVERT: ClassVar[int]
    GL_KEEP: ClassVar[int]
    GL_LEQUAL: ClassVar[int]
    GL_LESS: ClassVar[int]
    GL_LIGHT0: ClassVar[int]
    GL_LIGHT1: ClassVar[int]
    GL_LIGHT2: ClassVar[int]
    GL_LIGHT3: ClassVar[int]
    GL_LIGHT4: ClassVar[int]
    GL_LIGHT5: ClassVar[int]
    GL_LIGHT6: ClassVar[int]
    GL_LIGHT7: ClassVar[int]
    GL_LIGHTING: ClassVar[int]
    GL_LIGHT_MODEL_AMBIENT: ClassVar[int]
    GL_LIGHT_MODEL_TWO_SIDE: ClassVar[int]
    GL_LINEAR: ClassVar[int]
    GL_LINEAR_ATTENUATION: ClassVar[int]
    GL_LINEAR_MIPMAP_LINEAR: ClassVar[int]
    GL_LINEAR_MIPMAP_NEAREST: ClassVar[int]
    GL_LINES: ClassVar[int]
    GL_LINE_LOOP: ClassVar[int]
    GL_LINE_SMOOTH: ClassVar[int]
    GL_LINE_SMOOTH_HINT: ClassVar[int]
    GL_LINE_STRIP: ClassVar[int]
    GL_LUMINANCE: ClassVar[int]
    GL_LUMINANCE_ALPHA: ClassVar[int]
    GL_MAX_ELEMENTS_INDICES: ClassVar[int]
    GL_MAX_ELEMENTS_VERTICES: ClassVar[int]
    GL_MAX_LIGHTS: ClassVar[int]
    GL_MAX_MODELVIEW_STACK_DEPTH: ClassVar[int]
    GL_MAX_PROJECTION_STACK_DEPTH: ClassVar[int]
    GL_MAX_TEXTURE_SIZE: ClassVar[int]
    GL_MAX_TEXTURE_STACK_DEPTH: ClassVar[int]
    GL_MAX_TEXTURE_UNITS: ClassVar[int]
    GL_MAX_VIEWPORT_DIMS: ClassVar[int]
    GL_MODELVIEW: ClassVar[int]
    GL_MODULATE: ClassVar[int]
    GL_MULTISAMPLE: ClassVar[int]
    GL_NAND: ClassVar[int]
    GL_NEAREST: ClassVar[int]
    GL_NEAREST_MIPMAP_LINEAR: ClassVar[int]
    GL_NEAREST_MIPMAP_NEAREST: ClassVar[int]
    GL_NEVER: ClassVar[int]
    GL_NICEST: ClassVar[int]
    GL_NOOP: ClassVar[int]
    GL_NOR: ClassVar[int]
    GL_NORMALIZE: ClassVar[int]
    GL_NORMAL_ARRAY: ClassVar[int]
    GL_NOTEQUAL: ClassVar[int]
    GL_NO_ERROR: ClassVar[int]
    GL_NUM_COMPRESSED_TEXTURE_FORMATS: ClassVar[int]
    GL_ONE: ClassVar[int]
    GL_ONE_MINUS_DST_ALPHA: ClassVar[int]
    GL_ONE_MINUS_DST_COLOR: ClassVar[int]
    GL_ONE_MINUS_SRC_ALPHA: ClassVar[int]
    GL_ONE_MINUS_SRC_COLOR: ClassVar[int]
    GL_OR: ClassVar[int]
    GL_OR_INVERTED: ClassVar[int]
    GL_OR_REVERSE: ClassVar[int]
    GL_OUT_OF_MEMORY: ClassVar[int]
    GL_PACK_ALIGNMENT: ClassVar[int]
    GL_PALETTE4_R5_G6_B5_OES: ClassVar[int]
    GL_PALETTE4_RGB5_A1_OES: ClassVar[int]
    GL_PALETTE4_RGB8_OES: ClassVar[int]
    GL_PALETTE4_RGBA4_OES: ClassVar[int]
    GL_PALETTE4_RGBA8_OES: ClassVar[int]
    GL_PALETTE8_R5_G6_B5_OES: ClassVar[int]
    GL_PALETTE8_RGB5_A1_OES: ClassVar[int]
    GL_PALETTE8_RGB8_OES: ClassVar[int]
    GL_PALETTE8_RGBA4_OES: ClassVar[int]
    GL_PALETTE8_RGBA8_OES: ClassVar[int]
    GL_PERSPECTIVE_CORRECTION_HINT: ClassVar[int]
    GL_POINTS: ClassVar[int]
    GL_POINT_FADE_THRESHOLD_SIZE: ClassVar[int]
    GL_POINT_SIZE: ClassVar[int]
    GL_POINT_SMOOTH: ClassVar[int]
    GL_POINT_SMOOTH_HINT: ClassVar[int]
    GL_POLYGON_OFFSET_FILL: ClassVar[int]
    GL_POLYGON_SMOOTH_HINT: ClassVar[int]
    GL_POSITION: ClassVar[int]
    GL_PROJECTION: ClassVar[int]
    GL_QUADRATIC_ATTENUATION: ClassVar[int]
    GL_RED_BITS: ClassVar[int]
    GL_RENDERER: ClassVar[int]
    GL_REPEAT: ClassVar[int]
    GL_REPLACE: ClassVar[int]
    GL_RESCALE_NORMAL: ClassVar[int]
    GL_RGB: ClassVar[int]
    GL_RGBA: ClassVar[int]
    GL_SAMPLE_ALPHA_TO_COVERAGE: ClassVar[int]
    GL_SAMPLE_ALPHA_TO_ONE: ClassVar[int]
    GL_SAMPLE_COVERAGE: ClassVar[int]
    GL_SCISSOR_TEST: ClassVar[int]
    GL_SET: ClassVar[int]
    GL_SHININESS: ClassVar[int]
    GL_SHORT: ClassVar[int]
    GL_SMOOTH: ClassVar[int]
    GL_SMOOTH_LINE_WIDTH_RANGE: ClassVar[int]
    GL_SMOOTH_POINT_SIZE_RANGE: ClassVar[int]
    GL_SPECULAR: ClassVar[int]
    GL_SPOT_CUTOFF: ClassVar[int]
    GL_SPOT_DIRECTION: ClassVar[int]
    GL_SPOT_EXPONENT: ClassVar[int]
    GL_SRC_ALPHA: ClassVar[int]
    GL_SRC_ALPHA_SATURATE: ClassVar[int]
    GL_SRC_COLOR: ClassVar[int]
    GL_STACK_OVERFLOW: ClassVar[int]
    GL_STACK_UNDERFLOW: ClassVar[int]
    GL_STENCIL_BITS: ClassVar[int]
    GL_STENCIL_BUFFER_BIT: ClassVar[int]
    GL_STENCIL_TEST: ClassVar[int]
    GL_SUBPIXEL_BITS: ClassVar[int]
    GL_TEXTURE: ClassVar[int]
    GL_TEXTURE0: ClassVar[int]
    GL_TEXTURE1: ClassVar[int]
    GL_TEXTURE10: ClassVar[int]
    GL_TEXTURE11: ClassVar[int]
    GL_TEXTURE12: ClassVar[int]
    GL_TEXTURE13: ClassVar[int]
    GL_TEXTURE14: ClassVar[int]
    GL_TEXTURE15: ClassVar[int]
    GL_TEXTURE16: ClassVar[int]
    GL_TEXTURE17: ClassVar[int]
    GL_TEXTURE18: ClassVar[int]
    GL_TEXTURE19: ClassVar[int]
    GL_TEXTURE2: ClassVar[int]
    GL_TEXTURE20: ClassVar[int]
    GL_TEXTURE21: ClassVar[int]
    GL_TEXTURE22: ClassVar[int]
    GL_TEXTURE23: ClassVar[int]
    GL_TEXTURE24: ClassVar[int]
    GL_TEXTURE25: ClassVar[int]
    GL_TEXTURE26: ClassVar[int]
    GL_TEXTURE27: ClassVar[int]
    GL_TEXTURE28: ClassVar[int]
    GL_TEXTURE29: ClassVar[int]
    GL_TEXTURE3: ClassVar[int]
    GL_TEXTURE30: ClassVar[int]
    GL_TEXTURE31: ClassVar[int]
    GL_TEXTURE4: ClassVar[int]
    GL_TEXTURE5: ClassVar[int]
    GL_TEXTURE6: ClassVar[int]
    GL_TEXTURE7: ClassVar[int]
    GL_TEXTURE8: ClassVar[int]
    GL_TEXTURE9: ClassVar[int]
    GL_TEXTURE_2D: ClassVar[int]
    GL_TEXTURE_COORD_ARRAY: ClassVar[int]
    GL_TEXTURE_ENV: ClassVar[int]
    GL_TEXTURE_ENV_COLOR: ClassVar[int]
    GL_TEXTURE_ENV_MODE: ClassVar[int]
    GL_TEXTURE_MAG_FILTER: ClassVar[int]
    GL_TEXTURE_MIN_FILTER: ClassVar[int]
    GL_TEXTURE_WRAP_S: ClassVar[int]
    GL_TEXTURE_WRAP_T: ClassVar[int]
    GL_TRIANGLES: ClassVar[int]
    GL_TRIANGLE_FAN: ClassVar[int]
    GL_TRIANGLE_STRIP: ClassVar[int]
    GL_TRUE: ClassVar[int]
    GL_UNPACK_ALIGNMENT: ClassVar[int]
    GL_UNSIGNED_BYTE: ClassVar[int]
    GL_UNSIGNED_SHORT: ClassVar[int]
    GL_UNSIGNED_SHORT_4_4_4_4: ClassVar[int]
    GL_UNSIGNED_SHORT_5_5_5_1: ClassVar[int]
    GL_UNSIGNED_SHORT_5_6_5: ClassVar[int]
    GL_VENDOR: ClassVar[int]
    GL_VERSION: ClassVar[int]
    GL_VERTEX_ARRAY: ClassVar[int]
    GL_XOR: ClassVar[int]
    GL_ZERO: ClassVar[int]
    def __init__(self) -> None: ...
    @staticmethod
    def glBindBuffer(p0: int, p1: int) -> None: ...
    @staticmethod
    def glBufferData(p0: int, p1: int, p2: Buffer, p3: int) -> None: ...
    @staticmethod
    def glBufferSubData(p0: int, p1: int, p2: int, p3: Buffer) -> None: ...
    @overload
    @staticmethod
    def glDeleteBuffers(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteBuffers(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGenBuffers(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glGenBuffers(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetBooleanv(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glGetBooleanv(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetBufferParameteriv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetBufferParameteriv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetFloatv(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glGetFloatv(p0: int, p1: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameterfv(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameterfv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameteriv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameteriv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @staticmethod
    def glIsBuffer(p0: int) -> bool: ...
    @staticmethod
    def glIsEnabled(p0: int) -> bool: ...
    @staticmethod
    def glIsTexture(p0: int) -> bool: ...
    @overload
    @staticmethod
    def glTexParameterfv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glTexParameterfv(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @staticmethod
    def glTexParameteri(p0: int, p1: int, p2: int) -> None: ...
    @overload
    @staticmethod
    def glTexParameteriv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glTexParameteriv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glClipPlanef(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glClipPlanef(p0: int, p1: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glClipPlanex(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glClipPlanex(p0: int, p1: IntBuffer) -> None: ...
    @staticmethod
    def glColor4ub(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetClipPlanef(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glGetClipPlanef(p0: int, p1: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetClipPlanex(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetClipPlanex(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glGetFixedv(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glGetFixedv(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetLightfv(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetLightfv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetLightxv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetLightxv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetMaterialfv(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetMaterialfv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetMaterialxv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetMaterialxv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexEnvfv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexEnvfv(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexEnviv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexEnviv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexEnvxv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexEnvxv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameterxv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameterxv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def glPointParameterf(p0: int, p1: float) -> None: ...
    @overload
    @staticmethod
    def glPointParameterfv(p0: int, p1: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glPointParameterfv(p0: int, p1: Any, p2: int) -> None: ...
    @staticmethod
    def glPointParameterx(p0: int, p1: int) -> None: ...
    @overload
    @staticmethod
    def glPointParameterxv(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glPointParameterxv(p0: int, p1: Any, p2: int) -> None: ...
    @staticmethod
    def glPointSizePointerOES(p0: int, p1: int, p2: Buffer) -> None: ...
    @staticmethod
    def glTexEnvi(p0: int, p1: int, p2: int) -> None: ...
    @overload
    @staticmethod
    def glTexEnviv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glTexEnviv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glTexParameterxv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glTexParameterxv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @staticmethod
    def glColorPointer(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glDrawElements(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glNormalPointer(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glTexCoordPointer(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glVertexPointer(p0: int, p1: int, p2: int, p3: int) -> None: ...

from typing import Any, ClassVar, overload
from android.opengl.EGLConfig import EGLConfig
from android.opengl.EGLContext import EGLContext
from android.opengl.EGLDisplay import EGLDisplay
from android.opengl.EGLSurface import EGLSurface

class EGL14:
    EGL_ALPHA_MASK_SIZE: ClassVar[int]
    EGL_ALPHA_SIZE: ClassVar[int]
    EGL_BACK_BUFFER: ClassVar[int]
    EGL_BAD_ACCESS: ClassVar[int]
    EGL_BAD_ALLOC: ClassVar[int]
    EGL_BAD_ATTRIBUTE: ClassVar[int]
    EGL_BAD_CONFIG: ClassVar[int]
    EGL_BAD_CONTEXT: ClassVar[int]
    EGL_BAD_CURRENT_SURFACE: ClassVar[int]
    EGL_BAD_DISPLAY: ClassVar[int]
    EGL_BAD_MATCH: ClassVar[int]
    EGL_BAD_NATIVE_PIXMAP: ClassVar[int]
    EGL_BAD_NATIVE_WINDOW: ClassVar[int]
    EGL_BAD_PARAMETER: ClassVar[int]
    EGL_BAD_SURFACE: ClassVar[int]
    EGL_BIND_TO_TEXTURE_RGB: ClassVar[int]
    EGL_BIND_TO_TEXTURE_RGBA: ClassVar[int]
    EGL_BLUE_SIZE: ClassVar[int]
    EGL_BUFFER_DESTROYED: ClassVar[int]
    EGL_BUFFER_PRESERVED: ClassVar[int]
    EGL_BUFFER_SIZE: ClassVar[int]
    EGL_CLIENT_APIS: ClassVar[int]
    EGL_COLOR_BUFFER_TYPE: ClassVar[int]
    EGL_CONFIG_CAVEAT: ClassVar[int]
    EGL_CONFIG_ID: ClassVar[int]
    EGL_CONFORMANT: ClassVar[int]
    EGL_CONTEXT_CLIENT_TYPE: ClassVar[int]
    EGL_CONTEXT_CLIENT_VERSION: ClassVar[int]
    EGL_CONTEXT_LOST: ClassVar[int]
    EGL_CORE_NATIVE_ENGINE: ClassVar[int]
    EGL_DEFAULT_DISPLAY: ClassVar[int]
    EGL_DEPTH_SIZE: ClassVar[int]
    EGL_DISPLAY_SCALING: ClassVar[int]
    EGL_DRAW: ClassVar[int]
    EGL_EXTENSIONS: ClassVar[int]
    EGL_FALSE: ClassVar[int]
    EGL_GREEN_SIZE: ClassVar[int]
    EGL_HEIGHT: ClassVar[int]
    EGL_HORIZONTAL_RESOLUTION: ClassVar[int]
    EGL_LARGEST_PBUFFER: ClassVar[int]
    EGL_LEVEL: ClassVar[int]
    EGL_LUMINANCE_BUFFER: ClassVar[int]
    EGL_LUMINANCE_SIZE: ClassVar[int]
    EGL_MATCH_NATIVE_PIXMAP: ClassVar[int]
    EGL_MAX_PBUFFER_HEIGHT: ClassVar[int]
    EGL_MAX_PBUFFER_PIXELS: ClassVar[int]
    EGL_MAX_PBUFFER_WIDTH: ClassVar[int]
    EGL_MAX_SWAP_INTERVAL: ClassVar[int]
    EGL_MIN_SWAP_INTERVAL: ClassVar[int]
    EGL_MIPMAP_LEVEL: ClassVar[int]
    EGL_MIPMAP_TEXTURE: ClassVar[int]
    EGL_MULTISAMPLE_RESOLVE: ClassVar[int]
    EGL_MULTISAMPLE_RESOLVE_BOX: ClassVar[int]
    EGL_MULTISAMPLE_RESOLVE_BOX_BIT: ClassVar[int]
    EGL_MULTISAMPLE_RESOLVE_DEFAULT: ClassVar[int]
    EGL_NATIVE_RENDERABLE: ClassVar[int]
    EGL_NATIVE_VISUAL_ID: ClassVar[int]
    EGL_NATIVE_VISUAL_TYPE: ClassVar[int]
    EGL_NONE: ClassVar[int]
    EGL_NON_CONFORMANT_CONFIG: ClassVar[int]
    EGL_NOT_INITIALIZED: ClassVar[int]
    EGL_NO_CONTEXT: ClassVar[EGLContext]
    EGL_NO_DISPLAY: ClassVar[EGLDisplay]
    EGL_NO_SURFACE: ClassVar[EGLSurface]
    EGL_NO_TEXTURE: ClassVar[int]
    EGL_OPENGL_API: ClassVar[int]
    EGL_OPENGL_BIT: ClassVar[int]
    EGL_OPENGL_ES2_BIT: ClassVar[int]
    EGL_OPENGL_ES_API: ClassVar[int]
    EGL_OPENGL_ES_BIT: ClassVar[int]
    EGL_OPENVG_API: ClassVar[int]
    EGL_OPENVG_BIT: ClassVar[int]
    EGL_OPENVG_IMAGE: ClassVar[int]
    EGL_PBUFFER_BIT: ClassVar[int]
    EGL_PIXEL_ASPECT_RATIO: ClassVar[int]
    EGL_PIXMAP_BIT: ClassVar[int]
    EGL_READ: ClassVar[int]
    EGL_RED_SIZE: ClassVar[int]
    EGL_RENDERABLE_TYPE: ClassVar[int]
    EGL_RENDER_BUFFER: ClassVar[int]
    EGL_RGB_BUFFER: ClassVar[int]
    EGL_SAMPLES: ClassVar[int]
    EGL_SAMPLE_BUFFERS: ClassVar[int]
    EGL_SINGLE_BUFFER: ClassVar[int]
    EGL_SLOW_CONFIG: ClassVar[int]
    EGL_STENCIL_SIZE: ClassVar[int]
    EGL_SUCCESS: ClassVar[int]
    EGL_SURFACE_TYPE: ClassVar[int]
    EGL_SWAP_BEHAVIOR: ClassVar[int]
    EGL_SWAP_BEHAVIOR_PRESERVED_BIT: ClassVar[int]
    EGL_TEXTURE_2D: ClassVar[int]
    EGL_TEXTURE_FORMAT: ClassVar[int]
    EGL_TEXTURE_RGB: ClassVar[int]
    EGL_TEXTURE_RGBA: ClassVar[int]
    EGL_TEXTURE_TARGET: ClassVar[int]
    EGL_TRANSPARENT_BLUE_VALUE: ClassVar[int]
    EGL_TRANSPARENT_GREEN_VALUE: ClassVar[int]
    EGL_TRANSPARENT_RED_VALUE: ClassVar[int]
    EGL_TRANSPARENT_RGB: ClassVar[int]
    EGL_TRANSPARENT_TYPE: ClassVar[int]
    EGL_TRUE: ClassVar[int]
    EGL_VENDOR: ClassVar[int]
    EGL_VERSION: ClassVar[int]
    EGL_VERTICAL_RESOLUTION: ClassVar[int]
    EGL_VG_ALPHA_FORMAT: ClassVar[int]
    EGL_VG_ALPHA_FORMAT_NONPRE: ClassVar[int]
    EGL_VG_ALPHA_FORMAT_PRE: ClassVar[int]
    EGL_VG_ALPHA_FORMAT_PRE_BIT: ClassVar[int]
    EGL_VG_COLORSPACE: ClassVar[int]
    EGL_VG_COLORSPACE_LINEAR: ClassVar[int]
    EGL_VG_COLORSPACE_LINEAR_BIT: ClassVar[int]
    EGL_VG_COLORSPACE_sRGB: ClassVar[int]
    EGL_WIDTH: ClassVar[int]
    EGL_WINDOW_BIT: ClassVar[int]
    def __init__(self) -> None: ...
    @staticmethod
    def eglChooseConfig(p0: EGLDisplay, p1: Any, p2: int, p3: Any, p4: int, p5: int, p6: Any, p7: int) -> bool: ...
    @staticmethod
    def eglCopyBuffers(p0: EGLDisplay, p1: EGLSurface, p2: int) -> bool: ...
    @staticmethod
    def eglCreateContext(p0: EGLDisplay, p1: EGLConfig, p2: EGLContext, p3: Any, p4: int) -> EGLContext: ...
    @staticmethod
    def eglCreatePbufferSurface(p0: EGLDisplay, p1: EGLConfig, p2: Any, p3: int) -> EGLSurface: ...
    @staticmethod
    def eglCreatePixmapSurface(p0: EGLDisplay, p1: EGLConfig, p2: int, p3: Any, p4: int) -> EGLSurface: ...
    @staticmethod
    def eglCreateWindowSurface(p0: EGLDisplay, p1: EGLConfig, p2: Any, p3: Any, p4: int) -> EGLSurface: ...
    @staticmethod
    def eglDestroyContext(p0: EGLDisplay, p1: EGLContext) -> bool: ...
    @staticmethod
    def eglDestroySurface(p0: EGLDisplay, p1: EGLSurface) -> bool: ...
    @staticmethod
    def eglGetConfigAttrib(p0: EGLDisplay, p1: EGLConfig, p2: int, p3: Any, p4: int) -> bool: ...
    @staticmethod
    def eglGetConfigs(p0: EGLDisplay, p1: Any, p2: int, p3: int, p4: Any, p5: int) -> bool: ...
    @staticmethod
    def eglGetCurrentContext() -> EGLContext: ...
    @staticmethod
    def eglGetCurrentDisplay() -> EGLDisplay: ...
    @staticmethod
    def eglGetCurrentSurface(p0: int) -> EGLSurface: ...
    @staticmethod
    def eglGetDisplay(p0: int) -> EGLDisplay: ...
    @staticmethod
    def eglGetError() -> int: ...
    @staticmethod
    def eglInitialize(p0: EGLDisplay, p1: Any, p2: int, p3: Any, p4: int) -> bool: ...
    @staticmethod
    def eglMakeCurrent(p0: EGLDisplay, p1: EGLSurface, p2: EGLSurface, p3: EGLContext) -> bool: ...
    @staticmethod
    def eglQueryContext(p0: EGLDisplay, p1: EGLContext, p2: int, p3: Any, p4: int) -> bool: ...
    @staticmethod
    def eglQueryString(p0: EGLDisplay, p1: int) -> str: ...
    @staticmethod
    def eglQuerySurface(p0: EGLDisplay, p1: EGLSurface, p2: int, p3: Any, p4: int) -> bool: ...
    @staticmethod
    def eglSwapBuffers(p0: EGLDisplay, p1: EGLSurface) -> bool: ...
    @staticmethod
    def eglTerminate(p0: EGLDisplay) -> bool: ...
    @staticmethod
    def eglWaitGL() -> bool: ...
    @staticmethod
    def eglWaitNative(p0: int) -> bool: ...
    @staticmethod
    def eglBindAPI(p0: int) -> bool: ...
    @staticmethod
    def eglBindTexImage(p0: EGLDisplay, p1: EGLSurface, p2: int) -> bool: ...
    @staticmethod
    def eglCreatePbufferFromClientBuffer(p0: EGLDisplay, p1: int, p2: int, p3: EGLConfig, p4: Any, p5: int) -> EGLSurface: ...
    @staticmethod
    def eglQueryAPI() -> int: ...
    @staticmethod
    def eglReleaseTexImage(p0: EGLDisplay, p1: EGLSurface, p2: int) -> bool: ...
    @staticmethod
    def eglReleaseThread() -> bool: ...
    @staticmethod
    def eglSurfaceAttrib(p0: EGLDisplay, p1: EGLSurface, p2: int, p3: int) -> bool: ...
    @staticmethod
    def eglSwapInterval(p0: EGLDisplay, p1: int) -> bool: ...
    @staticmethod
    def eglWaitClient() -> bool: ...

from typing import Any, ClassVar, overload

class EGLDisplay:
    def equals(self, p0: Any) -> bool: ...

from typing import Any, ClassVar, overload

class EGLSurface:
    def equals(self, p0: Any) -> bool: ...

from typing import Any, ClassVar, overload
from java.nio.Buffer import Buffer
from java.nio.ByteBuffer import ByteBuffer
from java.nio.FloatBuffer import FloatBuffer
from java.nio.IntBuffer import IntBuffer
from java.nio.LongBuffer import LongBuffer

class GLES30:
    GL_ACTIVE_UNIFORM_BLOCKS: ClassVar[int]
    GL_ACTIVE_UNIFORM_BLOCK_MAX_NAME_LENGTH: ClassVar[int]
    GL_ALREADY_SIGNALED: ClassVar[int]
    GL_ANY_SAMPLES_PASSED: ClassVar[int]
    GL_ANY_SAMPLES_PASSED_CONSERVATIVE: ClassVar[int]
    GL_BLUE: ClassVar[int]
    GL_BUFFER_ACCESS_FLAGS: ClassVar[int]
    GL_BUFFER_MAPPED: ClassVar[int]
    GL_BUFFER_MAP_LENGTH: ClassVar[int]
    GL_BUFFER_MAP_OFFSET: ClassVar[int]
    GL_BUFFER_MAP_POINTER: ClassVar[int]
    GL_COLOR: ClassVar[int]
    GL_COLOR_ATTACHMENT1: ClassVar[int]
    GL_COLOR_ATTACHMENT10: ClassVar[int]
    GL_COLOR_ATTACHMENT11: ClassVar[int]
    GL_COLOR_ATTACHMENT12: ClassVar[int]
    GL_COLOR_ATTACHMENT13: ClassVar[int]
    GL_COLOR_ATTACHMENT14: ClassVar[int]
    GL_COLOR_ATTACHMENT15: ClassVar[int]
    GL_COLOR_ATTACHMENT2: ClassVar[int]
    GL_COLOR_ATTACHMENT3: ClassVar[int]
    GL_COLOR_ATTACHMENT4: ClassVar[int]
    GL_COLOR_ATTACHMENT5: ClassVar[int]
    GL_COLOR_ATTACHMENT6: ClassVar[int]
    GL_COLOR_ATTACHMENT7: ClassVar[int]
    GL_COLOR_ATTACHMENT8: ClassVar[int]
    GL_COLOR_ATTACHMENT9: ClassVar[int]
    GL_COMPARE_REF_TO_TEXTURE: ClassVar[int]
    GL_COMPRESSED_R11_EAC: ClassVar[int]
    GL_COMPRESSED_RG11_EAC: ClassVar[int]
    GL_COMPRESSED_RGB8_ETC2: ClassVar[int]
    GL_COMPRESSED_RGB8_PUNCHTHROUGH_ALPHA1_ETC2: ClassVar[int]
    GL_COMPRESSED_RGBA8_ETC2_EAC: ClassVar[int]
    GL_COMPRESSED_SIGNED_R11_EAC: ClassVar[int]
    GL_COMPRESSED_SIGNED_RG11_EAC: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ETC2_EAC: ClassVar[int]
    GL_COMPRESSED_SRGB8_ETC2: ClassVar[int]
    GL_COMPRESSED_SRGB8_PUNCHTHROUGH_ALPHA1_ETC2: ClassVar[int]
    GL_CONDITION_SATISFIED: ClassVar[int]
    GL_COPY_READ_BUFFER: ClassVar[int]
    GL_COPY_READ_BUFFER_BINDING: ClassVar[int]
    GL_COPY_WRITE_BUFFER: ClassVar[int]
    GL_COPY_WRITE_BUFFER_BINDING: ClassVar[int]
    GL_CURRENT_QUERY: ClassVar[int]
    GL_DEPTH: ClassVar[int]
    GL_DEPTH24_STENCIL8: ClassVar[int]
    GL_DEPTH32F_STENCIL8: ClassVar[int]
    GL_DEPTH_COMPONENT24: ClassVar[int]
    GL_DEPTH_COMPONENT32F: ClassVar[int]
    GL_DEPTH_STENCIL: ClassVar[int]
    GL_DEPTH_STENCIL_ATTACHMENT: ClassVar[int]
    GL_DRAW_BUFFER0: ClassVar[int]
    GL_DRAW_BUFFER1: ClassVar[int]
    GL_DRAW_BUFFER10: ClassVar[int]
    GL_DRAW_BUFFER11: ClassVar[int]
    GL_DRAW_BUFFER12: ClassVar[int]
    GL_DRAW_BUFFER13: ClassVar[int]
    GL_DRAW_BUFFER14: ClassVar[int]
    GL_DRAW_BUFFER15: ClassVar[int]
    GL_DRAW_BUFFER2: ClassVar[int]
    GL_DRAW_BUFFER3: ClassVar[int]
    GL_DRAW_BUFFER4: ClassVar[int]
    GL_DRAW_BUFFER5: ClassVar[int]
    GL_DRAW_BUFFER6: ClassVar[int]
    GL_DRAW_BUFFER7: ClassVar[int]
    GL_DRAW_BUFFER8: ClassVar[int]
    GL_DRAW_BUFFER9: ClassVar[int]
    GL_DRAW_FRAMEBUFFER: ClassVar[int]
    GL_DRAW_FRAMEBUFFER_BINDING: ClassVar[int]
    GL_DYNAMIC_COPY: ClassVar[int]
    GL_DYNAMIC_READ: ClassVar[int]
    GL_FLOAT_32_UNSIGNED_INT_24_8_REV: ClassVar[int]
    GL_FLOAT_MAT2x3: ClassVar[int]
    GL_FLOAT_MAT2x4: ClassVar[int]
    GL_FLOAT_MAT3x2: ClassVar[int]
    GL_FLOAT_MAT3x4: ClassVar[int]
    GL_FLOAT_MAT4x2: ClassVar[int]
    GL_FLOAT_MAT4x3: ClassVar[int]
    GL_FRAGMENT_SHADER_DERIVATIVE_HINT: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_ALPHA_SIZE: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_BLUE_SIZE: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_DEPTH_SIZE: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_GREEN_SIZE: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_RED_SIZE: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_STENCIL_SIZE: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER: ClassVar[int]
    GL_FRAMEBUFFER_DEFAULT: ClassVar[int]
    GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE: ClassVar[int]
    GL_FRAMEBUFFER_UNDEFINED: ClassVar[int]
    GL_GREEN: ClassVar[int]
    GL_HALF_FLOAT: ClassVar[int]
    GL_INTERLEAVED_ATTRIBS: ClassVar[int]
    GL_INT_2_10_10_10_REV: ClassVar[int]
    GL_INT_SAMPLER_2D: ClassVar[int]
    GL_INT_SAMPLER_2D_ARRAY: ClassVar[int]
    GL_INT_SAMPLER_3D: ClassVar[int]
    GL_INT_SAMPLER_CUBE: ClassVar[int]
    GL_INVALID_INDEX: ClassVar[int]
    GL_MAJOR_VERSION: ClassVar[int]
    GL_MAP_FLUSH_EXPLICIT_BIT: ClassVar[int]
    GL_MAP_INVALIDATE_BUFFER_BIT: ClassVar[int]
    GL_MAP_INVALIDATE_RANGE_BIT: ClassVar[int]
    GL_MAP_READ_BIT: ClassVar[int]
    GL_MAP_UNSYNCHRONIZED_BIT: ClassVar[int]
    GL_MAP_WRITE_BIT: ClassVar[int]
    GL_MAX: ClassVar[int]
    GL_MAX_3D_TEXTURE_SIZE: ClassVar[int]
    GL_MAX_ARRAY_TEXTURE_LAYERS: ClassVar[int]
    GL_MAX_COLOR_ATTACHMENTS: ClassVar[int]
    GL_MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS: ClassVar[int]
    GL_MAX_COMBINED_UNIFORM_BLOCKS: ClassVar[int]
    GL_MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS: ClassVar[int]
    GL_MAX_DRAW_BUFFERS: ClassVar[int]
    GL_MAX_ELEMENTS_INDICES: ClassVar[int]
    GL_MAX_ELEMENTS_VERTICES: ClassVar[int]
    GL_MAX_ELEMENT_INDEX: ClassVar[int]
    GL_MAX_FRAGMENT_INPUT_COMPONENTS: ClassVar[int]
    GL_MAX_FRAGMENT_UNIFORM_BLOCKS: ClassVar[int]
    GL_MAX_FRAGMENT_UNIFORM_COMPONENTS: ClassVar[int]
    GL_MAX_PROGRAM_TEXEL_OFFSET: ClassVar[int]
    GL_MAX_SAMPLES: ClassVar[int]
    GL_MAX_SERVER_WAIT_TIMEOUT: ClassVar[int]
    GL_MAX_TEXTURE_LOD_BIAS: ClassVar[int]
    GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS: ClassVar[int]
    GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS: ClassVar[int]
    GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS: ClassVar[int]
    GL_MAX_UNIFORM_BLOCK_SIZE: ClassVar[int]
    GL_MAX_UNIFORM_BUFFER_BINDINGS: ClassVar[int]
    GL_MAX_VARYING_COMPONENTS: ClassVar[int]
    GL_MAX_VERTEX_OUTPUT_COMPONENTS: ClassVar[int]
    GL_MAX_VERTEX_UNIFORM_BLOCKS: ClassVar[int]
    GL_MAX_VERTEX_UNIFORM_COMPONENTS: ClassVar[int]
    GL_MIN: ClassVar[int]
    GL_MINOR_VERSION: ClassVar[int]
    GL_MIN_PROGRAM_TEXEL_OFFSET: ClassVar[int]
    GL_NUM_EXTENSIONS: ClassVar[int]
    GL_NUM_PROGRAM_BINARY_FORMATS: ClassVar[int]
    GL_NUM_SAMPLE_COUNTS: ClassVar[int]
    GL_OBJECT_TYPE: ClassVar[int]
    GL_PACK_ROW_LENGTH: ClassVar[int]
    GL_PACK_SKIP_PIXELS: ClassVar[int]
    GL_PACK_SKIP_ROWS: ClassVar[int]
    GL_PIXEL_PACK_BUFFER: ClassVar[int]
    GL_PIXEL_PACK_BUFFER_BINDING: ClassVar[int]
    GL_PIXEL_UNPACK_BUFFER: ClassVar[int]
    GL_PIXEL_UNPACK_BUFFER_BINDING: ClassVar[int]
    GL_PRIMITIVE_RESTART_FIXED_INDEX: ClassVar[int]
    GL_PROGRAM_BINARY_FORMATS: ClassVar[int]
    GL_PROGRAM_BINARY_LENGTH: ClassVar[int]
    GL_PROGRAM_BINARY_RETRIEVABLE_HINT: ClassVar[int]
    GL_QUERY_RESULT: ClassVar[int]
    GL_QUERY_RESULT_AVAILABLE: ClassVar[int]
    GL_R11F_G11F_B10F: ClassVar[int]
    GL_R16F: ClassVar[int]
    GL_R16I: ClassVar[int]
    GL_R16UI: ClassVar[int]
    GL_R32F: ClassVar[int]
    GL_R32I: ClassVar[int]
    GL_R32UI: ClassVar[int]
    GL_R8: ClassVar[int]
    GL_R8I: ClassVar[int]
    GL_R8UI: ClassVar[int]
    GL_R8_SNORM: ClassVar[int]
    GL_RASTERIZER_DISCARD: ClassVar[int]
    GL_READ_BUFFER: ClassVar[int]
    GL_READ_FRAMEBUFFER: ClassVar[int]
    GL_READ_FRAMEBUFFER_BINDING: ClassVar[int]
    GL_RED: ClassVar[int]
    GL_RED_INTEGER: ClassVar[int]
    GL_RENDERBUFFER_SAMPLES: ClassVar[int]
    GL_RG: ClassVar[int]
    GL_RG16F: ClassVar[int]
    GL_RG16I: ClassVar[int]
    GL_RG16UI: ClassVar[int]
    GL_RG32F: ClassVar[int]
    GL_RG32I: ClassVar[int]
    GL_RG32UI: ClassVar[int]
    GL_RG8: ClassVar[int]
    GL_RG8I: ClassVar[int]
    GL_RG8UI: ClassVar[int]
    GL_RG8_SNORM: ClassVar[int]
    GL_RGB10_A2: ClassVar[int]
    GL_RGB10_A2UI: ClassVar[int]
    GL_RGB16F: ClassVar[int]
    GL_RGB16I: ClassVar[int]
    GL_RGB16UI: ClassVar[int]
    GL_RGB32F: ClassVar[int]
    GL_RGB32I: ClassVar[int]
    GL_RGB32UI: ClassVar[int]
    GL_RGB8: ClassVar[int]
    GL_RGB8I: ClassVar[int]
    GL_RGB8UI: ClassVar[int]
    GL_RGB8_SNORM: ClassVar[int]
    GL_RGB9_E5: ClassVar[int]
    GL_RGBA16F: ClassVar[int]
    GL_RGBA16I: ClassVar[int]
    GL_RGBA16UI: ClassVar[int]
    GL_RGBA32F: ClassVar[int]
    GL_RGBA32I: ClassVar[int]
    GL_RGBA32UI: ClassVar[int]
    GL_RGBA8: ClassVar[int]
    GL_RGBA8I: ClassVar[int]
    GL_RGBA8UI: ClassVar[int]
    GL_RGBA8_SNORM: ClassVar[int]
    GL_RGBA_INTEGER: ClassVar[int]
    GL_RGB_INTEGER: ClassVar[int]
    GL_RG_INTEGER: ClassVar[int]
    GL_SAMPLER_2D_ARRAY: ClassVar[int]
    GL_SAMPLER_2D_ARRAY_SHADOW: ClassVar[int]
    GL_SAMPLER_2D_SHADOW: ClassVar[int]
    GL_SAMPLER_3D: ClassVar[int]
    GL_SAMPLER_BINDING: ClassVar[int]
    GL_SAMPLER_CUBE_SHADOW: ClassVar[int]
    GL_SEPARATE_ATTRIBS: ClassVar[int]
    GL_SIGNALED: ClassVar[int]
    GL_SIGNED_NORMALIZED: ClassVar[int]
    GL_SRGB: ClassVar[int]
    GL_SRGB8: ClassVar[int]
    GL_SRGB8_ALPHA8: ClassVar[int]
    GL_STATIC_COPY: ClassVar[int]
    GL_STATIC_READ: ClassVar[int]
    GL_STENCIL: ClassVar[int]
    GL_STREAM_COPY: ClassVar[int]
    GL_STREAM_READ: ClassVar[int]
    GL_SYNC_CONDITION: ClassVar[int]
    GL_SYNC_FENCE: ClassVar[int]
    GL_SYNC_FLAGS: ClassVar[int]
    GL_SYNC_FLUSH_COMMANDS_BIT: ClassVar[int]
    GL_SYNC_GPU_COMMANDS_COMPLETE: ClassVar[int]
    GL_SYNC_STATUS: ClassVar[int]
    GL_TEXTURE_2D_ARRAY: ClassVar[int]
    GL_TEXTURE_3D: ClassVar[int]
    GL_TEXTURE_BASE_LEVEL: ClassVar[int]
    GL_TEXTURE_BINDING_2D_ARRAY: ClassVar[int]
    GL_TEXTURE_BINDING_3D: ClassVar[int]
    GL_TEXTURE_COMPARE_FUNC: ClassVar[int]
    GL_TEXTURE_COMPARE_MODE: ClassVar[int]
    GL_TEXTURE_IMMUTABLE_FORMAT: ClassVar[int]
    GL_TEXTURE_IMMUTABLE_LEVELS: ClassVar[int]
    GL_TEXTURE_MAX_LEVEL: ClassVar[int]
    GL_TEXTURE_MAX_LOD: ClassVar[int]
    GL_TEXTURE_MIN_LOD: ClassVar[int]
    GL_TEXTURE_SWIZZLE_A: ClassVar[int]
    GL_TEXTURE_SWIZZLE_B: ClassVar[int]
    GL_TEXTURE_SWIZZLE_G: ClassVar[int]
    GL_TEXTURE_SWIZZLE_R: ClassVar[int]
    GL_TEXTURE_WRAP_R: ClassVar[int]
    GL_TIMEOUT_EXPIRED: ClassVar[int]
    GL_TIMEOUT_IGNORED: ClassVar[int]
    GL_TRANSFORM_FEEDBACK: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_ACTIVE: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_BINDING: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_BUFFER: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_BUFFER_BINDING: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_BUFFER_MODE: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_BUFFER_SIZE: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_BUFFER_START: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_PAUSED: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_VARYINGS: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH: ClassVar[int]
    GL_UNIFORM_ARRAY_STRIDE: ClassVar[int]
    GL_UNIFORM_BLOCK_ACTIVE_UNIFORMS: ClassVar[int]
    GL_UNIFORM_BLOCK_ACTIVE_UNIFORM_INDICES: ClassVar[int]
    GL_UNIFORM_BLOCK_BINDING: ClassVar[int]
    GL_UNIFORM_BLOCK_DATA_SIZE: ClassVar[int]
    GL_UNIFORM_BLOCK_INDEX: ClassVar[int]
    GL_UNIFORM_BLOCK_NAME_LENGTH: ClassVar[int]
    GL_UNIFORM_BLOCK_REFERENCED_BY_FRAGMENT_SHADER: ClassVar[int]
    GL_UNIFORM_BLOCK_REFERENCED_BY_VERTEX_SHADER: ClassVar[int]
    GL_UNIFORM_BUFFER: ClassVar[int]
    GL_UNIFORM_BUFFER_BINDING: ClassVar[int]
    GL_UNIFORM_BUFFER_OFFSET_ALIGNMENT: ClassVar[int]
    GL_UNIFORM_BUFFER_SIZE: ClassVar[int]
    GL_UNIFORM_BUFFER_START: ClassVar[int]
    GL_UNIFORM_IS_ROW_MAJOR: ClassVar[int]
    GL_UNIFORM_MATRIX_STRIDE: ClassVar[int]
    GL_UNIFORM_NAME_LENGTH: ClassVar[int]
    GL_UNIFORM_OFFSET: ClassVar[int]
    GL_UNIFORM_SIZE: ClassVar[int]
    GL_UNIFORM_TYPE: ClassVar[int]
    GL_UNPACK_IMAGE_HEIGHT: ClassVar[int]
    GL_UNPACK_ROW_LENGTH: ClassVar[int]
    GL_UNPACK_SKIP_IMAGES: ClassVar[int]
    GL_UNPACK_SKIP_PIXELS: ClassVar[int]
    GL_UNPACK_SKIP_ROWS: ClassVar[int]
    GL_UNSIGNALED: ClassVar[int]
    GL_UNSIGNED_INT_10F_11F_11F_REV: ClassVar[int]
    GL_UNSIGNED_INT_24_8: ClassVar[int]
    GL_UNSIGNED_INT_2_10_10_10_REV: ClassVar[int]
    GL_UNSIGNED_INT_5_9_9_9_REV: ClassVar[int]
    GL_UNSIGNED_INT_SAMPLER_2D: ClassVar[int]
    GL_UNSIGNED_INT_SAMPLER_2D_ARRAY: ClassVar[int]
    GL_UNSIGNED_INT_SAMPLER_3D: ClassVar[int]
    GL_UNSIGNED_INT_SAMPLER_CUBE: ClassVar[int]
    GL_UNSIGNED_INT_VEC2: ClassVar[int]
    GL_UNSIGNED_INT_VEC3: ClassVar[int]
    GL_UNSIGNED_INT_VEC4: ClassVar[int]
    GL_UNSIGNED_NORMALIZED: ClassVar[int]
    GL_VERTEX_ARRAY_BINDING: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_DIVISOR: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_INTEGER: ClassVar[int]
    GL_WAIT_FAILED: ClassVar[int]
    GL_ACTIVE_ATTRIBUTES: ClassVar[int]
    GL_ACTIVE_ATTRIBUTE_MAX_LENGTH: ClassVar[int]
    GL_ACTIVE_TEXTURE: ClassVar[int]
    GL_ACTIVE_UNIFORMS: ClassVar[int]
    GL_ACTIVE_UNIFORM_MAX_LENGTH: ClassVar[int]
    GL_ALIASED_LINE_WIDTH_RANGE: ClassVar[int]
    GL_ALIASED_POINT_SIZE_RANGE: ClassVar[int]
    GL_ALPHA: ClassVar[int]
    GL_ALPHA_BITS: ClassVar[int]
    GL_ALWAYS: ClassVar[int]
    GL_ARRAY_BUFFER: ClassVar[int]
    GL_ARRAY_BUFFER_BINDING: ClassVar[int]
    GL_ATTACHED_SHADERS: ClassVar[int]
    GL_BACK: ClassVar[int]
    GL_BLEND: ClassVar[int]
    GL_BLEND_COLOR: ClassVar[int]
    GL_BLEND_DST_ALPHA: ClassVar[int]
    GL_BLEND_DST_RGB: ClassVar[int]
    GL_BLEND_EQUATION: ClassVar[int]
    GL_BLEND_EQUATION_ALPHA: ClassVar[int]
    GL_BLEND_EQUATION_RGB: ClassVar[int]
    GL_BLEND_SRC_ALPHA: ClassVar[int]
    GL_BLEND_SRC_RGB: ClassVar[int]
    GL_BLUE_BITS: ClassVar[int]
    GL_BOOL: ClassVar[int]
    GL_BOOL_VEC2: ClassVar[int]
    GL_BOOL_VEC3: ClassVar[int]
    GL_BOOL_VEC4: ClassVar[int]
    GL_BUFFER_SIZE: ClassVar[int]
    GL_BUFFER_USAGE: ClassVar[int]
    GL_BYTE: ClassVar[int]
    GL_CCW: ClassVar[int]
    GL_CLAMP_TO_EDGE: ClassVar[int]
    GL_COLOR_ATTACHMENT0: ClassVar[int]
    GL_COLOR_BUFFER_BIT: ClassVar[int]
    GL_COLOR_CLEAR_VALUE: ClassVar[int]
    GL_COLOR_WRITEMASK: ClassVar[int]
    GL_COMPILE_STATUS: ClassVar[int]
    GL_COMPRESSED_TEXTURE_FORMATS: ClassVar[int]
    GL_CONSTANT_ALPHA: ClassVar[int]
    GL_CONSTANT_COLOR: ClassVar[int]
    GL_CULL_FACE: ClassVar[int]
    GL_CULL_FACE_MODE: ClassVar[int]
    GL_CURRENT_PROGRAM: ClassVar[int]
    GL_CURRENT_VERTEX_ATTRIB: ClassVar[int]
    GL_CW: ClassVar[int]
    GL_DECR: ClassVar[int]
    GL_DECR_WRAP: ClassVar[int]
    GL_DELETE_STATUS: ClassVar[int]
    GL_DEPTH_ATTACHMENT: ClassVar[int]
    GL_DEPTH_BITS: ClassVar[int]
    GL_DEPTH_BUFFER_BIT: ClassVar[int]
    GL_DEPTH_CLEAR_VALUE: ClassVar[int]
    GL_DEPTH_COMPONENT: ClassVar[int]
    GL_DEPTH_COMPONENT16: ClassVar[int]
    GL_DEPTH_FUNC: ClassVar[int]
    GL_DEPTH_RANGE: ClassVar[int]
    GL_DEPTH_TEST: ClassVar[int]
    GL_DEPTH_WRITEMASK: ClassVar[int]
    GL_DITHER: ClassVar[int]
    GL_DONT_CARE: ClassVar[int]
    GL_DST_ALPHA: ClassVar[int]
    GL_DST_COLOR: ClassVar[int]
    GL_DYNAMIC_DRAW: ClassVar[int]
    GL_ELEMENT_ARRAY_BUFFER: ClassVar[int]
    GL_ELEMENT_ARRAY_BUFFER_BINDING: ClassVar[int]
    GL_EQUAL: ClassVar[int]
    GL_EXTENSIONS: ClassVar[int]
    GL_FALSE: ClassVar[int]
    GL_FASTEST: ClassVar[int]
    GL_FIXED: ClassVar[int]
    GL_FLOAT: ClassVar[int]
    GL_FLOAT_MAT2: ClassVar[int]
    GL_FLOAT_MAT3: ClassVar[int]
    GL_FLOAT_MAT4: ClassVar[int]
    GL_FLOAT_VEC2: ClassVar[int]
    GL_FLOAT_VEC3: ClassVar[int]
    GL_FLOAT_VEC4: ClassVar[int]
    GL_FRAGMENT_SHADER: ClassVar[int]
    GL_FRAMEBUFFER: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL: ClassVar[int]
    GL_FRAMEBUFFER_BINDING: ClassVar[int]
    GL_FRAMEBUFFER_COMPLETE: ClassVar[int]
    GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT: ClassVar[int]
    GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS: ClassVar[int]
    GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT: ClassVar[int]
    GL_FRAMEBUFFER_UNSUPPORTED: ClassVar[int]
    GL_FRONT: ClassVar[int]
    GL_FRONT_AND_BACK: ClassVar[int]
    GL_FRONT_FACE: ClassVar[int]
    GL_FUNC_ADD: ClassVar[int]
    GL_FUNC_REVERSE_SUBTRACT: ClassVar[int]
    GL_FUNC_SUBTRACT: ClassVar[int]
    GL_GENERATE_MIPMAP_HINT: ClassVar[int]
    GL_GEQUAL: ClassVar[int]
    GL_GREATER: ClassVar[int]
    GL_GREEN_BITS: ClassVar[int]
    GL_HIGH_FLOAT: ClassVar[int]
    GL_HIGH_INT: ClassVar[int]
    GL_IMPLEMENTATION_COLOR_READ_FORMAT: ClassVar[int]
    GL_IMPLEMENTATION_COLOR_READ_TYPE: ClassVar[int]
    GL_INCR: ClassVar[int]
    GL_INCR_WRAP: ClassVar[int]
    GL_INFO_LOG_LENGTH: ClassVar[int]
    GL_INT: ClassVar[int]
    GL_INT_VEC2: ClassVar[int]
    GL_INT_VEC3: ClassVar[int]
    GL_INT_VEC4: ClassVar[int]
    GL_INVALID_ENUM: ClassVar[int]
    GL_INVALID_FRAMEBUFFER_OPERATION: ClassVar[int]
    GL_INVALID_OPERATION: ClassVar[int]
    GL_INVALID_VALUE: ClassVar[int]
    GL_INVERT: ClassVar[int]
    GL_KEEP: ClassVar[int]
    GL_LEQUAL: ClassVar[int]
    GL_LESS: ClassVar[int]
    GL_LINEAR: ClassVar[int]
    GL_LINEAR_MIPMAP_LINEAR: ClassVar[int]
    GL_LINEAR_MIPMAP_NEAREST: ClassVar[int]
    GL_LINES: ClassVar[int]
    GL_LINE_LOOP: ClassVar[int]
    GL_LINE_STRIP: ClassVar[int]
    GL_LINE_WIDTH: ClassVar[int]
    GL_LINK_STATUS: ClassVar[int]
    GL_LOW_FLOAT: ClassVar[int]
    GL_LOW_INT: ClassVar[int]
    GL_LUMINANCE: ClassVar[int]
    GL_LUMINANCE_ALPHA: ClassVar[int]
    GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS: ClassVar[int]
    GL_MAX_CUBE_MAP_TEXTURE_SIZE: ClassVar[int]
    GL_MAX_FRAGMENT_UNIFORM_VECTORS: ClassVar[int]
    GL_MAX_RENDERBUFFER_SIZE: ClassVar[int]
    GL_MAX_TEXTURE_IMAGE_UNITS: ClassVar[int]
    GL_MAX_TEXTURE_SIZE: ClassVar[int]
    GL_MAX_VARYING_VECTORS: ClassVar[int]
    GL_MAX_VERTEX_ATTRIBS: ClassVar[int]
    GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS: ClassVar[int]
    GL_MAX_VERTEX_UNIFORM_VECTORS: ClassVar[int]
    GL_MAX_VIEWPORT_DIMS: ClassVar[int]
    GL_MEDIUM_FLOAT: ClassVar[int]
    GL_MEDIUM_INT: ClassVar[int]
    GL_MIRRORED_REPEAT: ClassVar[int]
    GL_NEAREST: ClassVar[int]
    GL_NEAREST_MIPMAP_LINEAR: ClassVar[int]
    GL_NEAREST_MIPMAP_NEAREST: ClassVar[int]
    GL_NEVER: ClassVar[int]
    GL_NICEST: ClassVar[int]
    GL_NONE: ClassVar[int]
    GL_NOTEQUAL: ClassVar[int]
    GL_NO_ERROR: ClassVar[int]
    GL_NUM_COMPRESSED_TEXTURE_FORMATS: ClassVar[int]
    GL_NUM_SHADER_BINARY_FORMATS: ClassVar[int]
    GL_ONE: ClassVar[int]
    GL_ONE_MINUS_CONSTANT_ALPHA: ClassVar[int]
    GL_ONE_MINUS_CONSTANT_COLOR: ClassVar[int]
    GL_ONE_MINUS_DST_ALPHA: ClassVar[int]
    GL_ONE_MINUS_DST_COLOR: ClassVar[int]
    GL_ONE_MINUS_SRC_ALPHA: ClassVar[int]
    GL_ONE_MINUS_SRC_COLOR: ClassVar[int]
    GL_OUT_OF_MEMORY: ClassVar[int]
    GL_PACK_ALIGNMENT: ClassVar[int]
    GL_POINTS: ClassVar[int]
    GL_POLYGON_OFFSET_FACTOR: ClassVar[int]
    GL_POLYGON_OFFSET_FILL: ClassVar[int]
    GL_POLYGON_OFFSET_UNITS: ClassVar[int]
    GL_RED_BITS: ClassVar[int]
    GL_RENDERBUFFER: ClassVar[int]
    GL_RENDERBUFFER_ALPHA_SIZE: ClassVar[int]
    GL_RENDERBUFFER_BINDING: ClassVar[int]
    GL_RENDERBUFFER_BLUE_SIZE: ClassVar[int]
    GL_RENDERBUFFER_DEPTH_SIZE: ClassVar[int]
    GL_RENDERBUFFER_GREEN_SIZE: ClassVar[int]
    GL_RENDERBUFFER_HEIGHT: ClassVar[int]
    GL_RENDERBUFFER_INTERNAL_FORMAT: ClassVar[int]
    GL_RENDERBUFFER_RED_SIZE: ClassVar[int]
    GL_RENDERBUFFER_STENCIL_SIZE: ClassVar[int]
    GL_RENDERBUFFER_WIDTH: ClassVar[int]
    GL_RENDERER: ClassVar[int]
    GL_REPEAT: ClassVar[int]
    GL_REPLACE: ClassVar[int]
    GL_RGB: ClassVar[int]
    GL_RGB565: ClassVar[int]
    GL_RGB5_A1: ClassVar[int]
    GL_RGBA: ClassVar[int]
    GL_RGBA4: ClassVar[int]
    GL_SAMPLER_2D: ClassVar[int]
    GL_SAMPLER_CUBE: ClassVar[int]
    GL_SAMPLES: ClassVar[int]
    GL_SAMPLE_ALPHA_TO_COVERAGE: ClassVar[int]
    GL_SAMPLE_BUFFERS: ClassVar[int]
    GL_SAMPLE_COVERAGE: ClassVar[int]
    GL_SAMPLE_COVERAGE_INVERT: ClassVar[int]
    GL_SAMPLE_COVERAGE_VALUE: ClassVar[int]
    GL_SCISSOR_BOX: ClassVar[int]
    GL_SCISSOR_TEST: ClassVar[int]
    GL_SHADER_BINARY_FORMATS: ClassVar[int]
    GL_SHADER_COMPILER: ClassVar[int]
    GL_SHADER_SOURCE_LENGTH: ClassVar[int]
    GL_SHADER_TYPE: ClassVar[int]
    GL_SHADING_LANGUAGE_VERSION: ClassVar[int]
    GL_SHORT: ClassVar[int]
    GL_SRC_ALPHA: ClassVar[int]
    GL_SRC_ALPHA_SATURATE: ClassVar[int]
    GL_SRC_COLOR: ClassVar[int]
    GL_STATIC_DRAW: ClassVar[int]
    GL_STENCIL_ATTACHMENT: ClassVar[int]
    GL_STENCIL_BACK_FAIL: ClassVar[int]
    GL_STENCIL_BACK_FUNC: ClassVar[int]
    GL_STENCIL_BACK_PASS_DEPTH_FAIL: ClassVar[int]
    GL_STENCIL_BACK_PASS_DEPTH_PASS: ClassVar[int]
    GL_STENCIL_BACK_REF: ClassVar[int]
    GL_STENCIL_BACK_VALUE_MASK: ClassVar[int]
    GL_STENCIL_BACK_WRITEMASK: ClassVar[int]
    GL_STENCIL_BITS: ClassVar[int]
    GL_STENCIL_BUFFER_BIT: ClassVar[int]
    GL_STENCIL_CLEAR_VALUE: ClassVar[int]
    GL_STENCIL_FAIL: ClassVar[int]
    GL_STENCIL_FUNC: ClassVar[int]
    GL_STENCIL_INDEX: ClassVar[int]
    GL_STENCIL_INDEX8: ClassVar[int]
    GL_STENCIL_PASS_DEPTH_FAIL: ClassVar[int]
    GL_STENCIL_PASS_DEPTH_PASS: ClassVar[int]
    GL_STENCIL_REF: ClassVar[int]
    GL_STENCIL_TEST: ClassVar[int]
    GL_STENCIL_VALUE_MASK: ClassVar[int]
    GL_STENCIL_WRITEMASK: ClassVar[int]
    GL_STREAM_DRAW: ClassVar[int]
    GL_SUBPIXEL_BITS: ClassVar[int]
    GL_TEXTURE: ClassVar[int]
    GL_TEXTURE0: ClassVar[int]
    GL_TEXTURE1: ClassVar[int]
    GL_TEXTURE10: ClassVar[int]
    GL_TEXTURE11: ClassVar[int]
    GL_TEXTURE12: ClassVar[int]
    GL_TEXTURE13: ClassVar[int]
    GL_TEXTURE14: ClassVar[int]
    GL_TEXTURE15: ClassVar[int]
    GL_TEXTURE16: ClassVar[int]
    GL_TEXTURE17: ClassVar[int]
    GL_TEXTURE18: ClassVar[int]
    GL_TEXTURE19: ClassVar[int]
    GL_TEXTURE2: ClassVar[int]
    GL_TEXTURE20: ClassVar[int]
    GL_TEXTURE21: ClassVar[int]
    GL_TEXTURE22: ClassVar[int]
    GL_TEXTURE23: ClassVar[int]
    GL_TEXTURE24: ClassVar[int]
    GL_TEXTURE25: ClassVar[int]
    GL_TEXTURE26: ClassVar[int]
    GL_TEXTURE27: ClassVar[int]
    GL_TEXTURE28: ClassVar[int]
    GL_TEXTURE29: ClassVar[int]
    GL_TEXTURE3: ClassVar[int]
    GL_TEXTURE30: ClassVar[int]
    GL_TEXTURE31: ClassVar[int]
    GL_TEXTURE4: ClassVar[int]
    GL_TEXTURE5: ClassVar[int]
    GL_TEXTURE6: ClassVar[int]
    GL_TEXTURE7: ClassVar[int]
    GL_TEXTURE8: ClassVar[int]
    GL_TEXTURE9: ClassVar[int]
    GL_TEXTURE_2D: ClassVar[int]
    GL_TEXTURE_BINDING_2D: ClassVar[int]
    GL_TEXTURE_BINDING_CUBE_MAP: ClassVar[int]
    GL_TEXTURE_CUBE_MAP: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_NEGATIVE_X: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_NEGATIVE_Y: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_NEGATIVE_Z: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_POSITIVE_X: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_POSITIVE_Y: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_POSITIVE_Z: ClassVar[int]
    GL_TEXTURE_MAG_FILTER: ClassVar[int]
    GL_TEXTURE_MIN_FILTER: ClassVar[int]
    GL_TEXTURE_WRAP_S: ClassVar[int]
    GL_TEXTURE_WRAP_T: ClassVar[int]
    GL_TRIANGLES: ClassVar[int]
    GL_TRIANGLE_FAN: ClassVar[int]
    GL_TRIANGLE_STRIP: ClassVar[int]
    GL_TRUE: ClassVar[int]
    GL_UNPACK_ALIGNMENT: ClassVar[int]
    GL_UNSIGNED_BYTE: ClassVar[int]
    GL_UNSIGNED_INT: ClassVar[int]
    GL_UNSIGNED_SHORT: ClassVar[int]
    GL_UNSIGNED_SHORT_4_4_4_4: ClassVar[int]
    GL_UNSIGNED_SHORT_5_5_5_1: ClassVar[int]
    GL_UNSIGNED_SHORT_5_6_5: ClassVar[int]
    GL_VALIDATE_STATUS: ClassVar[int]
    GL_VENDOR: ClassVar[int]
    GL_VERSION: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_ENABLED: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_NORMALIZED: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_POINTER: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_SIZE: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_STRIDE: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_TYPE: ClassVar[int]
    GL_VERTEX_SHADER: ClassVar[int]
    GL_VIEWPORT: ClassVar[int]
    GL_ZERO: ClassVar[int]
    def __init__(self) -> None: ...
    @staticmethod
    def glBeginQuery(p0: int, p1: int) -> None: ...
    @staticmethod
    def glBeginTransformFeedback(p0: int) -> None: ...
    @staticmethod
    def glBindBufferBase(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glBindBufferRange(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @staticmethod
    def glBindSampler(p0: int, p1: int) -> None: ...
    @staticmethod
    def glBindTransformFeedback(p0: int, p1: int) -> None: ...
    @staticmethod
    def glBindVertexArray(p0: int) -> None: ...
    @staticmethod
    def glBlitFramebuffer(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: int, p9: int) -> None: ...
    @staticmethod
    def glClearBufferfi(p0: int, p1: int, p2: float, p3: int) -> None: ...
    @overload
    @staticmethod
    def glClearBufferfv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glClearBufferfv(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glClearBufferiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glClearBufferiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glClearBufferuiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glClearBufferuiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def glClientWaitSync(p0: int, p1: int, p2: int) -> int: ...
    @overload
    @staticmethod
    def glCompressedTexImage3D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: int) -> None: ...
    @overload
    @staticmethod
    def glCompressedTexImage3D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: Buffer) -> None: ...
    @overload
    @staticmethod
    def glCompressedTexSubImage3D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: int, p9: int, p10: int) -> None: ...
    @overload
    @staticmethod
    def glCompressedTexSubImage3D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: int, p9: int, p10: Buffer) -> None: ...
    @staticmethod
    def glCopyBufferSubData(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @staticmethod
    def glCopyTexSubImage3D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteQueries(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glDeleteQueries(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteSamplers(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glDeleteSamplers(p0: int, p1: Any, p2: int) -> None: ...
    @staticmethod
    def glDeleteSync(p0: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteTransformFeedbacks(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteTransformFeedbacks(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glDeleteVertexArrays(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glDeleteVertexArrays(p0: int, p1: Any, p2: int) -> None: ...
    @staticmethod
    def glDrawArraysInstanced(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @overload
    @staticmethod
    def glDrawBuffers(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glDrawBuffers(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glDrawElementsInstanced(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @overload
    @staticmethod
    def glDrawElementsInstanced(p0: int, p1: int, p2: int, p3: Buffer, p4: int) -> None: ...
    @overload
    @staticmethod
    def glDrawRangeElements(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int) -> None: ...
    @overload
    @staticmethod
    def glDrawRangeElements(p0: int, p1: int, p2: int, p3: int, p4: int, p5: Buffer) -> None: ...
    @staticmethod
    def glEndQuery(p0: int) -> None: ...
    @staticmethod
    def glEndTransformFeedback() -> None: ...
    @staticmethod
    def glFenceSync(p0: int, p1: int) -> int: ...
    @staticmethod
    def glFlushMappedBufferRange(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glFramebufferTextureLayer(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @overload
    @staticmethod
    def glGenQueries(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGenQueries(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glGenSamplers(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGenSamplers(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glGenTransformFeedbacks(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGenTransformFeedbacks(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glGenVertexArrays(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glGenVertexArrays(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetActiveUniformBlockName(p0: int, p1: int, p2: int, p3: Any, p4: int, p5: Any, p6: int) -> None: ...
    @overload
    @staticmethod
    def glGetActiveUniformBlockName(p0: int, p1: int) -> str: ...
    @overload
    @staticmethod
    def glGetActiveUniformBlockName(p0: int, p1: int, p2: Buffer, p3: Buffer) -> None: ...
    @overload
    @staticmethod
    def glGetActiveUniformBlockiv(p0: int, p1: int, p2: int, p3: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetActiveUniformBlockiv(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glGetActiveUniformsiv(p0: int, p1: int, p2: Any, p3: int, p4: int, p5: Any, p6: int) -> None: ...
    @overload
    @staticmethod
    def glGetActiveUniformsiv(p0: int, p1: int, p2: IntBuffer, p3: int, p4: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetBufferParameteri64v(p0: int, p1: int, p2: LongBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetBufferParameteri64v(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def glGetBufferPointerv(p0: int, p1: int) -> Buffer: ...
    @staticmethod
    def glGetFragDataLocation(p0: int, p1: str) -> int: ...
    @overload
    @staticmethod
    def glGetInteger64i_v(p0: int, p1: int, p2: LongBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetInteger64i_v(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetInteger64v(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glGetInteger64v(p0: int, p1: LongBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetIntegeri_v(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetIntegeri_v(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetInternalformativ(p0: int, p1: int, p2: int, p3: int, p4: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetInternalformativ(p0: int, p1: int, p2: int, p3: int, p4: Any, p5: int) -> None: ...
    @overload
    @staticmethod
    def glGetProgramBinary(p0: int, p1: int, p2: Any, p3: int, p4: Any, p5: int, p6: Buffer) -> None: ...
    @overload
    @staticmethod
    def glGetProgramBinary(p0: int, p1: int, p2: IntBuffer, p3: IntBuffer, p4: Buffer) -> None: ...
    @overload
    @staticmethod
    def glGetQueryObjectuiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetQueryObjectuiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetQueryiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetQueryiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetSamplerParameterfv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetSamplerParameterfv(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetSamplerParameteriv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetSamplerParameteriv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @staticmethod
    def glGetStringi(p0: int, p1: int) -> str: ...
    @overload
    @staticmethod
    def glGetSynciv(p0: int, p1: int, p2: int, p3: IntBuffer, p4: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetSynciv(p0: int, p1: int, p2: int, p3: Any, p4: int, p5: Any, p6: int) -> None: ...
    @overload
    @staticmethod
    def glGetTransformFeedbackVarying(p0: int, p1: int, p2: int, p3: IntBuffer, p4: IntBuffer, p5: IntBuffer, p6: int) -> None: ...
    @overload
    @staticmethod
    def glGetTransformFeedbackVarying(p0: int, p1: int, p2: IntBuffer, p3: IntBuffer) -> str: ...
    @overload
    @staticmethod
    def glGetTransformFeedbackVarying(p0: int, p1: int, p2: Any, p3: int, p4: Any, p5: int) -> str: ...
    @overload
    @staticmethod
    def glGetTransformFeedbackVarying(p0: int, p1: int, p2: int, p3: Any, p4: int, p5: Any, p6: int, p7: Any, p8: int, p9: Any, p10: int) -> None: ...
    @overload
    @staticmethod
    def glGetTransformFeedbackVarying(p0: int, p1: int, p2: int, p3: IntBuffer, p4: IntBuffer, p5: IntBuffer, p6: ByteBuffer) -> None: ...
    @staticmethod
    def glGetUniformBlockIndex(p0: int, p1: str) -> int: ...
    @overload
    @staticmethod
    def glGetUniformIndices(p0: int, p1: Any, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetUniformIndices(p0: int, p1: Any, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetUniformuiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetUniformuiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetVertexAttribIiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetVertexAttribIiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetVertexAttribIuiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetVertexAttribIuiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glInvalidateFramebuffer(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glInvalidateFramebuffer(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glInvalidateSubFramebuffer(p0: int, p1: int, p2: Any, p3: int, p4: int, p5: int, p6: int, p7: int) -> None: ...
    @overload
    @staticmethod
    def glInvalidateSubFramebuffer(p0: int, p1: int, p2: IntBuffer, p3: int, p4: int, p5: int, p6: int) -> None: ...
    @staticmethod
    def glIsQuery(p0: int) -> bool: ...
    @staticmethod
    def glIsSampler(p0: int) -> bool: ...
    @staticmethod
    def glIsSync(p0: int) -> bool: ...
    @staticmethod
    def glIsTransformFeedback(p0: int) -> bool: ...
    @staticmethod
    def glIsVertexArray(p0: int) -> bool: ...
    @staticmethod
    def glMapBufferRange(p0: int, p1: int, p2: int, p3: int) -> Buffer: ...
    @staticmethod
    def glPauseTransformFeedback() -> None: ...
    @staticmethod
    def glProgramBinary(p0: int, p1: int, p2: Buffer, p3: int) -> None: ...
    @staticmethod
    def glProgramParameteri(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glReadBuffer(p0: int) -> None: ...
    @staticmethod
    def glRenderbufferStorageMultisample(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @staticmethod
    def glResumeTransformFeedback() -> None: ...
    @staticmethod
    def glSamplerParameterf(p0: int, p1: int, p2: float) -> None: ...
    @overload
    @staticmethod
    def glSamplerParameterfv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glSamplerParameterfv(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @staticmethod
    def glSamplerParameteri(p0: int, p1: int, p2: int) -> None: ...
    @overload
    @staticmethod
    def glSamplerParameteriv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glSamplerParameteriv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glTexImage3D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: int, p9: Buffer) -> None: ...
    @overload
    @staticmethod
    def glTexImage3D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: int, p9: int) -> None: ...
    @staticmethod
    def glTexStorage2D(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @staticmethod
    def glTexStorage3D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int) -> None: ...
    @overload
    @staticmethod
    def glTexSubImage3D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: int, p9: int, p10: Buffer) -> None: ...
    @overload
    @staticmethod
    def glTexSubImage3D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: int, p9: int, p10: int) -> None: ...
    @staticmethod
    def glTransformFeedbackVaryings(p0: int, p1: Any, p2: int) -> None: ...
    @staticmethod
    def glUniform1ui(p0: int, p1: int) -> None: ...
    @overload
    @staticmethod
    def glUniform1uiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniform1uiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def glUniform2ui(p0: int, p1: int, p2: int) -> None: ...
    @overload
    @staticmethod
    def glUniform2uiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniform2uiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def glUniform3ui(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @overload
    @staticmethod
    def glUniform3uiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glUniform3uiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @staticmethod
    def glUniform4ui(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @overload
    @staticmethod
    def glUniform4uiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glUniform4uiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @staticmethod
    def glUniformBlockBinding(p0: int, p1: int, p2: int) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix2x3fv(p0: int, p1: int, p2: bool, p3: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix2x3fv(p0: int, p1: int, p2: bool, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix2x4fv(p0: int, p1: int, p2: bool, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix2x4fv(p0: int, p1: int, p2: bool, p3: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix3x2fv(p0: int, p1: int, p2: bool, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix3x2fv(p0: int, p1: int, p2: bool, p3: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix3x4fv(p0: int, p1: int, p2: bool, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix3x4fv(p0: int, p1: int, p2: bool, p3: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix4x2fv(p0: int, p1: int, p2: bool, p3: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix4x2fv(p0: int, p1: int, p2: bool, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix4x3fv(p0: int, p1: int, p2: bool, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix4x3fv(p0: int, p1: int, p2: bool, p3: FloatBuffer) -> None: ...
    @staticmethod
    def glUnmapBuffer(p0: int) -> bool: ...
    @staticmethod
    def glVertexAttribDivisor(p0: int, p1: int) -> None: ...
    @staticmethod
    def glVertexAttribI4i(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @overload
    @staticmethod
    def glVertexAttribI4iv(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glVertexAttribI4iv(p0: int, p1: IntBuffer) -> None: ...
    @staticmethod
    def glVertexAttribI4ui(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @overload
    @staticmethod
    def glVertexAttribI4uiv(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glVertexAttribI4uiv(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glVertexAttribIPointer(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @overload
    @staticmethod
    def glVertexAttribIPointer(p0: int, p1: int, p2: int, p3: int, p4: Buffer) -> None: ...
    @staticmethod
    def glWaitSync(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glReadPixels(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int) -> None: ...

from typing import Any, ClassVar, overload
from java.io.Writer import Writer
from javax.microedition.khronos.egl.EGL import EGL
from javax.microedition.khronos.opengles.GL import GL

class GLDebugHelper:
    CONFIG_CHECK_GL_ERROR: ClassVar[int]
    CONFIG_CHECK_THREAD: ClassVar[int]
    CONFIG_LOG_ARGUMENT_NAMES: ClassVar[int]
    ERROR_WRONG_THREAD: ClassVar[int]
    def __init__(self) -> None: ...
    @overload
    @staticmethod
    def wrap(p0: EGL, p1: int, p2: Writer) -> EGL: ...
    @overload
    @staticmethod
    def wrap(p0: GL, p1: int, p2: Writer) -> GL: ...

from typing import Any, ClassVar, overload

class Matrix:
    def __init__(self) -> None: ...
    @overload
    @staticmethod
    def scaleM(p0: Any, p1: int, p2: float, p3: float, p4: float) -> None: ...
    @overload
    @staticmethod
    def scaleM(p0: Any, p1: int, p2: Any, p3: int, p4: float, p5: float, p6: float) -> None: ...
    @staticmethod
    def orthoM(p0: Any, p1: int, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float) -> None: ...
    @staticmethod
    def invertM(p0: Any, p1: int, p2: Any, p3: int) -> bool: ...
    @staticmethod
    def multiplyMM(p0: Any, p1: int, p2: Any, p3: int, p4: Any, p5: int) -> None: ...
    @staticmethod
    def multiplyMV(p0: Any, p1: int, p2: Any, p3: int, p4: Any, p5: int) -> None: ...
    @staticmethod
    def frustumM(p0: Any, p1: int, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float) -> None: ...
    @staticmethod
    def perspectiveM(p0: Any, p1: int, p2: float, p3: float, p4: float, p5: float) -> None: ...
    @overload
    @staticmethod
    def rotateM(p0: Any, p1: int, p2: Any, p3: int, p4: float, p5: float, p6: float, p7: float) -> None: ...
    @overload
    @staticmethod
    def rotateM(p0: Any, p1: int, p2: float, p3: float, p4: float, p5: float) -> None: ...
    @staticmethod
    def setIdentityM(p0: Any, p1: int) -> None: ...
    @staticmethod
    def setLookAtM(p0: Any, p1: int, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float, p8: float, p9: float, p10: float) -> None: ...
    @staticmethod
    def setRotateEulerM(p0: Any, p1: int, p2: float, p3: float, p4: float) -> None: ...
    @staticmethod
    def setRotateEulerM2(p0: Any, p1: int, p2: float, p3: float, p4: float) -> None: ...
    @staticmethod
    def setRotateM(p0: Any, p1: int, p2: float, p3: float, p4: float, p5: float) -> None: ...
    @overload
    @staticmethod
    def translateM(p0: Any, p1: int, p2: float, p3: float, p4: float) -> None: ...
    @overload
    @staticmethod
    def translateM(p0: Any, p1: int, p2: Any, p3: int, p4: float, p5: float, p6: float) -> None: ...
    @staticmethod
    def transposeM(p0: Any, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def length(p0: float, p1: float, p2: float) -> float: ...

from typing import Any, ClassVar, overload

class EGLContext:
    def equals(self, p0: Any) -> bool: ...

from typing import Any, ClassVar, overload

class EGLImage:
    def equals(self, p0: Any) -> bool: ...

from typing import Any, ClassVar, overload

class GLException:
    @overload
    def __init__(self, p0: int) -> None: ...
    @overload
    def __init__(self, p0: int, p1: str) -> None: ...

from typing import Any, ClassVar, overload
from java.nio.Buffer import Buffer
from java.nio.FloatBuffer import FloatBuffer
from java.nio.IntBuffer import IntBuffer

class GLES20:
    GL_ACTIVE_ATTRIBUTES: ClassVar[int]
    GL_ACTIVE_ATTRIBUTE_MAX_LENGTH: ClassVar[int]
    GL_ACTIVE_TEXTURE: ClassVar[int]
    GL_ACTIVE_UNIFORMS: ClassVar[int]
    GL_ACTIVE_UNIFORM_MAX_LENGTH: ClassVar[int]
    GL_ALIASED_LINE_WIDTH_RANGE: ClassVar[int]
    GL_ALIASED_POINT_SIZE_RANGE: ClassVar[int]
    GL_ALPHA: ClassVar[int]
    GL_ALPHA_BITS: ClassVar[int]
    GL_ALWAYS: ClassVar[int]
    GL_ARRAY_BUFFER: ClassVar[int]
    GL_ARRAY_BUFFER_BINDING: ClassVar[int]
    GL_ATTACHED_SHADERS: ClassVar[int]
    GL_BACK: ClassVar[int]
    GL_BLEND: ClassVar[int]
    GL_BLEND_COLOR: ClassVar[int]
    GL_BLEND_DST_ALPHA: ClassVar[int]
    GL_BLEND_DST_RGB: ClassVar[int]
    GL_BLEND_EQUATION: ClassVar[int]
    GL_BLEND_EQUATION_ALPHA: ClassVar[int]
    GL_BLEND_EQUATION_RGB: ClassVar[int]
    GL_BLEND_SRC_ALPHA: ClassVar[int]
    GL_BLEND_SRC_RGB: ClassVar[int]
    GL_BLUE_BITS: ClassVar[int]
    GL_BOOL: ClassVar[int]
    GL_BOOL_VEC2: ClassVar[int]
    GL_BOOL_VEC3: ClassVar[int]
    GL_BOOL_VEC4: ClassVar[int]
    GL_BUFFER_SIZE: ClassVar[int]
    GL_BUFFER_USAGE: ClassVar[int]
    GL_BYTE: ClassVar[int]
    GL_CCW: ClassVar[int]
    GL_CLAMP_TO_EDGE: ClassVar[int]
    GL_COLOR_ATTACHMENT0: ClassVar[int]
    GL_COLOR_BUFFER_BIT: ClassVar[int]
    GL_COLOR_CLEAR_VALUE: ClassVar[int]
    GL_COLOR_WRITEMASK: ClassVar[int]
    GL_COMPILE_STATUS: ClassVar[int]
    GL_COMPRESSED_TEXTURE_FORMATS: ClassVar[int]
    GL_CONSTANT_ALPHA: ClassVar[int]
    GL_CONSTANT_COLOR: ClassVar[int]
    GL_CULL_FACE: ClassVar[int]
    GL_CULL_FACE_MODE: ClassVar[int]
    GL_CURRENT_PROGRAM: ClassVar[int]
    GL_CURRENT_VERTEX_ATTRIB: ClassVar[int]
    GL_CW: ClassVar[int]
    GL_DECR: ClassVar[int]
    GL_DECR_WRAP: ClassVar[int]
    GL_DELETE_STATUS: ClassVar[int]
    GL_DEPTH_ATTACHMENT: ClassVar[int]
    GL_DEPTH_BITS: ClassVar[int]
    GL_DEPTH_BUFFER_BIT: ClassVar[int]
    GL_DEPTH_CLEAR_VALUE: ClassVar[int]
    GL_DEPTH_COMPONENT: ClassVar[int]
    GL_DEPTH_COMPONENT16: ClassVar[int]
    GL_DEPTH_FUNC: ClassVar[int]
    GL_DEPTH_RANGE: ClassVar[int]
    GL_DEPTH_TEST: ClassVar[int]
    GL_DEPTH_WRITEMASK: ClassVar[int]
    GL_DITHER: ClassVar[int]
    GL_DONT_CARE: ClassVar[int]
    GL_DST_ALPHA: ClassVar[int]
    GL_DST_COLOR: ClassVar[int]
    GL_DYNAMIC_DRAW: ClassVar[int]
    GL_ELEMENT_ARRAY_BUFFER: ClassVar[int]
    GL_ELEMENT_ARRAY_BUFFER_BINDING: ClassVar[int]
    GL_EQUAL: ClassVar[int]
    GL_EXTENSIONS: ClassVar[int]
    GL_FALSE: ClassVar[int]
    GL_FASTEST: ClassVar[int]
    GL_FIXED: ClassVar[int]
    GL_FLOAT: ClassVar[int]
    GL_FLOAT_MAT2: ClassVar[int]
    GL_FLOAT_MAT3: ClassVar[int]
    GL_FLOAT_MAT4: ClassVar[int]
    GL_FLOAT_VEC2: ClassVar[int]
    GL_FLOAT_VEC3: ClassVar[int]
    GL_FLOAT_VEC4: ClassVar[int]
    GL_FRAGMENT_SHADER: ClassVar[int]
    GL_FRAMEBUFFER: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL: ClassVar[int]
    GL_FRAMEBUFFER_BINDING: ClassVar[int]
    GL_FRAMEBUFFER_COMPLETE: ClassVar[int]
    GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT: ClassVar[int]
    GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS: ClassVar[int]
    GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT: ClassVar[int]
    GL_FRAMEBUFFER_UNSUPPORTED: ClassVar[int]
    GL_FRONT: ClassVar[int]
    GL_FRONT_AND_BACK: ClassVar[int]
    GL_FRONT_FACE: ClassVar[int]
    GL_FUNC_ADD: ClassVar[int]
    GL_FUNC_REVERSE_SUBTRACT: ClassVar[int]
    GL_FUNC_SUBTRACT: ClassVar[int]
    GL_GENERATE_MIPMAP_HINT: ClassVar[int]
    GL_GEQUAL: ClassVar[int]
    GL_GREATER: ClassVar[int]
    GL_GREEN_BITS: ClassVar[int]
    GL_HIGH_FLOAT: ClassVar[int]
    GL_HIGH_INT: ClassVar[int]
    GL_IMPLEMENTATION_COLOR_READ_FORMAT: ClassVar[int]
    GL_IMPLEMENTATION_COLOR_READ_TYPE: ClassVar[int]
    GL_INCR: ClassVar[int]
    GL_INCR_WRAP: ClassVar[int]
    GL_INFO_LOG_LENGTH: ClassVar[int]
    GL_INT: ClassVar[int]
    GL_INT_VEC2: ClassVar[int]
    GL_INT_VEC3: ClassVar[int]
    GL_INT_VEC4: ClassVar[int]
    GL_INVALID_ENUM: ClassVar[int]
    GL_INVALID_FRAMEBUFFER_OPERATION: ClassVar[int]
    GL_INVALID_OPERATION: ClassVar[int]
    GL_INVALID_VALUE: ClassVar[int]
    GL_INVERT: ClassVar[int]
    GL_KEEP: ClassVar[int]
    GL_LEQUAL: ClassVar[int]
    GL_LESS: ClassVar[int]
    GL_LINEAR: ClassVar[int]
    GL_LINEAR_MIPMAP_LINEAR: ClassVar[int]
    GL_LINEAR_MIPMAP_NEAREST: ClassVar[int]
    GL_LINES: ClassVar[int]
    GL_LINE_LOOP: ClassVar[int]
    GL_LINE_STRIP: ClassVar[int]
    GL_LINE_WIDTH: ClassVar[int]
    GL_LINK_STATUS: ClassVar[int]
    GL_LOW_FLOAT: ClassVar[int]
    GL_LOW_INT: ClassVar[int]
    GL_LUMINANCE: ClassVar[int]
    GL_LUMINANCE_ALPHA: ClassVar[int]
    GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS: ClassVar[int]
    GL_MAX_CUBE_MAP_TEXTURE_SIZE: ClassVar[int]
    GL_MAX_FRAGMENT_UNIFORM_VECTORS: ClassVar[int]
    GL_MAX_RENDERBUFFER_SIZE: ClassVar[int]
    GL_MAX_TEXTURE_IMAGE_UNITS: ClassVar[int]
    GL_MAX_TEXTURE_SIZE: ClassVar[int]
    GL_MAX_VARYING_VECTORS: ClassVar[int]
    GL_MAX_VERTEX_ATTRIBS: ClassVar[int]
    GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS: ClassVar[int]
    GL_MAX_VERTEX_UNIFORM_VECTORS: ClassVar[int]
    GL_MAX_VIEWPORT_DIMS: ClassVar[int]
    GL_MEDIUM_FLOAT: ClassVar[int]
    GL_MEDIUM_INT: ClassVar[int]
    GL_MIRRORED_REPEAT: ClassVar[int]
    GL_NEAREST: ClassVar[int]
    GL_NEAREST_MIPMAP_LINEAR: ClassVar[int]
    GL_NEAREST_MIPMAP_NEAREST: ClassVar[int]
    GL_NEVER: ClassVar[int]
    GL_NICEST: ClassVar[int]
    GL_NONE: ClassVar[int]
    GL_NOTEQUAL: ClassVar[int]
    GL_NO_ERROR: ClassVar[int]
    GL_NUM_COMPRESSED_TEXTURE_FORMATS: ClassVar[int]
    GL_NUM_SHADER_BINARY_FORMATS: ClassVar[int]
    GL_ONE: ClassVar[int]
    GL_ONE_MINUS_CONSTANT_ALPHA: ClassVar[int]
    GL_ONE_MINUS_CONSTANT_COLOR: ClassVar[int]
    GL_ONE_MINUS_DST_ALPHA: ClassVar[int]
    GL_ONE_MINUS_DST_COLOR: ClassVar[int]
    GL_ONE_MINUS_SRC_ALPHA: ClassVar[int]
    GL_ONE_MINUS_SRC_COLOR: ClassVar[int]
    GL_OUT_OF_MEMORY: ClassVar[int]
    GL_PACK_ALIGNMENT: ClassVar[int]
    GL_POINTS: ClassVar[int]
    GL_POLYGON_OFFSET_FACTOR: ClassVar[int]
    GL_POLYGON_OFFSET_FILL: ClassVar[int]
    GL_POLYGON_OFFSET_UNITS: ClassVar[int]
    GL_RED_BITS: ClassVar[int]
    GL_RENDERBUFFER: ClassVar[int]
    GL_RENDERBUFFER_ALPHA_SIZE: ClassVar[int]
    GL_RENDERBUFFER_BINDING: ClassVar[int]
    GL_RENDERBUFFER_BLUE_SIZE: ClassVar[int]
    GL_RENDERBUFFER_DEPTH_SIZE: ClassVar[int]
    GL_RENDERBUFFER_GREEN_SIZE: ClassVar[int]
    GL_RENDERBUFFER_HEIGHT: ClassVar[int]
    GL_RENDERBUFFER_INTERNAL_FORMAT: ClassVar[int]
    GL_RENDERBUFFER_RED_SIZE: ClassVar[int]
    GL_RENDERBUFFER_STENCIL_SIZE: ClassVar[int]
    GL_RENDERBUFFER_WIDTH: ClassVar[int]
    GL_RENDERER: ClassVar[int]
    GL_REPEAT: ClassVar[int]
    GL_REPLACE: ClassVar[int]
    GL_RGB: ClassVar[int]
    GL_RGB565: ClassVar[int]
    GL_RGB5_A1: ClassVar[int]
    GL_RGBA: ClassVar[int]
    GL_RGBA4: ClassVar[int]
    GL_SAMPLER_2D: ClassVar[int]
    GL_SAMPLER_CUBE: ClassVar[int]
    GL_SAMPLES: ClassVar[int]
    GL_SAMPLE_ALPHA_TO_COVERAGE: ClassVar[int]
    GL_SAMPLE_BUFFERS: ClassVar[int]
    GL_SAMPLE_COVERAGE: ClassVar[int]
    GL_SAMPLE_COVERAGE_INVERT: ClassVar[int]
    GL_SAMPLE_COVERAGE_VALUE: ClassVar[int]
    GL_SCISSOR_BOX: ClassVar[int]
    GL_SCISSOR_TEST: ClassVar[int]
    GL_SHADER_BINARY_FORMATS: ClassVar[int]
    GL_SHADER_COMPILER: ClassVar[int]
    GL_SHADER_SOURCE_LENGTH: ClassVar[int]
    GL_SHADER_TYPE: ClassVar[int]
    GL_SHADING_LANGUAGE_VERSION: ClassVar[int]
    GL_SHORT: ClassVar[int]
    GL_SRC_ALPHA: ClassVar[int]
    GL_SRC_ALPHA_SATURATE: ClassVar[int]
    GL_SRC_COLOR: ClassVar[int]
    GL_STATIC_DRAW: ClassVar[int]
    GL_STENCIL_ATTACHMENT: ClassVar[int]
    GL_STENCIL_BACK_FAIL: ClassVar[int]
    GL_STENCIL_BACK_FUNC: ClassVar[int]
    GL_STENCIL_BACK_PASS_DEPTH_FAIL: ClassVar[int]
    GL_STENCIL_BACK_PASS_DEPTH_PASS: ClassVar[int]
    GL_STENCIL_BACK_REF: ClassVar[int]
    GL_STENCIL_BACK_VALUE_MASK: ClassVar[int]
    GL_STENCIL_BACK_WRITEMASK: ClassVar[int]
    GL_STENCIL_BITS: ClassVar[int]
    GL_STENCIL_BUFFER_BIT: ClassVar[int]
    GL_STENCIL_CLEAR_VALUE: ClassVar[int]
    GL_STENCIL_FAIL: ClassVar[int]
    GL_STENCIL_FUNC: ClassVar[int]
    GL_STENCIL_INDEX: ClassVar[int]
    GL_STENCIL_INDEX8: ClassVar[int]
    GL_STENCIL_PASS_DEPTH_FAIL: ClassVar[int]
    GL_STENCIL_PASS_DEPTH_PASS: ClassVar[int]
    GL_STENCIL_REF: ClassVar[int]
    GL_STENCIL_TEST: ClassVar[int]
    GL_STENCIL_VALUE_MASK: ClassVar[int]
    GL_STENCIL_WRITEMASK: ClassVar[int]
    GL_STREAM_DRAW: ClassVar[int]
    GL_SUBPIXEL_BITS: ClassVar[int]
    GL_TEXTURE: ClassVar[int]
    GL_TEXTURE0: ClassVar[int]
    GL_TEXTURE1: ClassVar[int]
    GL_TEXTURE10: ClassVar[int]
    GL_TEXTURE11: ClassVar[int]
    GL_TEXTURE12: ClassVar[int]
    GL_TEXTURE13: ClassVar[int]
    GL_TEXTURE14: ClassVar[int]
    GL_TEXTURE15: ClassVar[int]
    GL_TEXTURE16: ClassVar[int]
    GL_TEXTURE17: ClassVar[int]
    GL_TEXTURE18: ClassVar[int]
    GL_TEXTURE19: ClassVar[int]
    GL_TEXTURE2: ClassVar[int]
    GL_TEXTURE20: ClassVar[int]
    GL_TEXTURE21: ClassVar[int]
    GL_TEXTURE22: ClassVar[int]
    GL_TEXTURE23: ClassVar[int]
    GL_TEXTURE24: ClassVar[int]
    GL_TEXTURE25: ClassVar[int]
    GL_TEXTURE26: ClassVar[int]
    GL_TEXTURE27: ClassVar[int]
    GL_TEXTURE28: ClassVar[int]
    GL_TEXTURE29: ClassVar[int]
    GL_TEXTURE3: ClassVar[int]
    GL_TEXTURE30: ClassVar[int]
    GL_TEXTURE31: ClassVar[int]
    GL_TEXTURE4: ClassVar[int]
    GL_TEXTURE5: ClassVar[int]
    GL_TEXTURE6: ClassVar[int]
    GL_TEXTURE7: ClassVar[int]
    GL_TEXTURE8: ClassVar[int]
    GL_TEXTURE9: ClassVar[int]
    GL_TEXTURE_2D: ClassVar[int]
    GL_TEXTURE_BINDING_2D: ClassVar[int]
    GL_TEXTURE_BINDING_CUBE_MAP: ClassVar[int]
    GL_TEXTURE_CUBE_MAP: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_NEGATIVE_X: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_NEGATIVE_Y: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_NEGATIVE_Z: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_POSITIVE_X: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_POSITIVE_Y: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_POSITIVE_Z: ClassVar[int]
    GL_TEXTURE_MAG_FILTER: ClassVar[int]
    GL_TEXTURE_MIN_FILTER: ClassVar[int]
    GL_TEXTURE_WRAP_S: ClassVar[int]
    GL_TEXTURE_WRAP_T: ClassVar[int]
    GL_TRIANGLES: ClassVar[int]
    GL_TRIANGLE_FAN: ClassVar[int]
    GL_TRIANGLE_STRIP: ClassVar[int]
    GL_TRUE: ClassVar[int]
    GL_UNPACK_ALIGNMENT: ClassVar[int]
    GL_UNSIGNED_BYTE: ClassVar[int]
    GL_UNSIGNED_INT: ClassVar[int]
    GL_UNSIGNED_SHORT: ClassVar[int]
    GL_UNSIGNED_SHORT_4_4_4_4: ClassVar[int]
    GL_UNSIGNED_SHORT_5_5_5_1: ClassVar[int]
    GL_UNSIGNED_SHORT_5_6_5: ClassVar[int]
    GL_VALIDATE_STATUS: ClassVar[int]
    GL_VENDOR: ClassVar[int]
    GL_VERSION: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_ENABLED: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_NORMALIZED: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_POINTER: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_SIZE: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_STRIDE: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_TYPE: ClassVar[int]
    GL_VERTEX_SHADER: ClassVar[int]
    GL_VIEWPORT: ClassVar[int]
    GL_ZERO: ClassVar[int]
    def __init__(self) -> None: ...
    @staticmethod
    def glAttachShader(p0: int, p1: int) -> None: ...
    @staticmethod
    def glBindAttribLocation(p0: int, p1: int, p2: str) -> None: ...
    @staticmethod
    def glBindBuffer(p0: int, p1: int) -> None: ...
    @staticmethod
    def glBindFramebuffer(p0: int, p1: int) -> None: ...
    @staticmethod
    def glBindRenderbuffer(p0: int, p1: int) -> None: ...
    @staticmethod
    def glBlendColor(p0: float, p1: float, p2: float, p3: float) -> None: ...
    @staticmethod
    def glBlendEquation(p0: int) -> None: ...
    @staticmethod
    def glBlendEquationSeparate(p0: int, p1: int) -> None: ...
    @staticmethod
    def glBlendFuncSeparate(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glBufferData(p0: int, p1: int, p2: Buffer, p3: int) -> None: ...
    @staticmethod
    def glBufferSubData(p0: int, p1: int, p2: int, p3: Buffer) -> None: ...
    @staticmethod
    def glCheckFramebufferStatus(p0: int) -> int: ...
    @staticmethod
    def glCompileShader(p0: int) -> None: ...
    @staticmethod
    def glCreateProgram() -> int: ...
    @staticmethod
    def glCreateShader(p0: int) -> int: ...
    @overload
    @staticmethod
    def glDeleteBuffers(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteBuffers(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glDeleteFramebuffers(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteFramebuffers(p0: int, p1: IntBuffer) -> None: ...
    @staticmethod
    def glDeleteProgram(p0: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteRenderbuffers(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glDeleteRenderbuffers(p0: int, p1: Any, p2: int) -> None: ...
    @staticmethod
    def glDeleteShader(p0: int) -> None: ...
    @staticmethod
    def glDetachShader(p0: int, p1: int) -> None: ...
    @staticmethod
    def glDisableVertexAttribArray(p0: int) -> None: ...
    @staticmethod
    def glEnableVertexAttribArray(p0: int) -> None: ...
    @staticmethod
    def glFramebufferRenderbuffer(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glFramebufferTexture2D(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @overload
    @staticmethod
    def glGenBuffers(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glGenBuffers(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGenFramebuffers(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glGenFramebuffers(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGenRenderbuffers(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGenRenderbuffers(p0: int, p1: Any, p2: int) -> None: ...
    @staticmethod
    def glGenerateMipmap(p0: int) -> None: ...
    @overload
    @staticmethod
    def glGetActiveAttrib(p0: int, p1: int, p2: IntBuffer, p3: IntBuffer) -> str: ...
    @overload
    @staticmethod
    def glGetActiveAttrib(p0: int, p1: int, p2: Any, p3: int, p4: Any, p5: int) -> str: ...
    @overload
    @staticmethod
    def glGetActiveAttrib(p0: int, p1: int, p2: int, p3: Any, p4: int, p5: Any, p6: int, p7: Any, p8: int, p9: Any, p10: int) -> None: ...
    @overload
    @staticmethod
    def glGetActiveUniform(p0: int, p1: int, p2: IntBuffer, p3: IntBuffer) -> str: ...
    @overload
    @staticmethod
    def glGetActiveUniform(p0: int, p1: int, p2: Any, p3: int, p4: Any, p5: int) -> str: ...
    @overload
    @staticmethod
    def glGetActiveUniform(p0: int, p1: int, p2: int, p3: Any, p4: int, p5: Any, p6: int, p7: Any, p8: int, p9: Any, p10: int) -> None: ...
    @overload
    @staticmethod
    def glGetAttachedShaders(p0: int, p1: int, p2: IntBuffer, p3: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetAttachedShaders(p0: int, p1: int, p2: Any, p3: int, p4: Any, p5: int) -> None: ...
    @staticmethod
    def glGetAttribLocation(p0: int, p1: str) -> int: ...
    @overload
    @staticmethod
    def glGetBooleanv(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetBooleanv(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glGetBufferParameteriv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetBufferParameteriv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetFloatv(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glGetFloatv(p0: int, p1: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetFramebufferAttachmentParameteriv(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glGetFramebufferAttachmentParameteriv(p0: int, p1: int, p2: int, p3: IntBuffer) -> None: ...
    @staticmethod
    def glGetProgramInfoLog(p0: int) -> str: ...
    @overload
    @staticmethod
    def glGetProgramiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetProgramiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetRenderbufferParameteriv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetRenderbufferParameteriv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @staticmethod
    def glGetShaderInfoLog(p0: int) -> str: ...
    @overload
    @staticmethod
    def glGetShaderPrecisionFormat(p0: int, p1: int, p2: IntBuffer, p3: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetShaderPrecisionFormat(p0: int, p1: int, p2: Any, p3: int, p4: Any, p5: int) -> None: ...
    @overload
    @staticmethod
    def glGetShaderSource(p0: int) -> str: ...
    @overload
    @staticmethod
    def glGetShaderSource(p0: int, p1: int, p2: Any, p3: int, p4: Any, p5: int) -> None: ...
    @overload
    @staticmethod
    def glGetShaderiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetShaderiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameterfv(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameterfv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameteriv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameteriv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def glGetUniformLocation(p0: int, p1: str) -> int: ...
    @overload
    @staticmethod
    def glGetUniformfv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetUniformfv(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetUniformiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetUniformiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetVertexAttribfv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetVertexAttribfv(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetVertexAttribiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetVertexAttribiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def glIsBuffer(p0: int) -> bool: ...
    @staticmethod
    def glIsEnabled(p0: int) -> bool: ...
    @staticmethod
    def glIsFramebuffer(p0: int) -> bool: ...
    @staticmethod
    def glIsProgram(p0: int) -> bool: ...
    @staticmethod
    def glIsRenderbuffer(p0: int) -> bool: ...
    @staticmethod
    def glIsShader(p0: int) -> bool: ...
    @staticmethod
    def glIsTexture(p0: int) -> bool: ...
    @staticmethod
    def glLinkProgram(p0: int) -> None: ...
    @staticmethod
    def glReleaseShaderCompiler() -> None: ...
    @staticmethod
    def glRenderbufferStorage(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @overload
    @staticmethod
    def glShaderBinary(p0: int, p1: IntBuffer, p2: int, p3: Buffer, p4: int) -> None: ...
    @overload
    @staticmethod
    def glShaderBinary(p0: int, p1: Any, p2: int, p3: int, p4: Buffer, p5: int) -> None: ...
    @staticmethod
    def glShaderSource(p0: int, p1: str) -> None: ...
    @staticmethod
    def glStencilFuncSeparate(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glStencilMaskSeparate(p0: int, p1: int) -> None: ...
    @staticmethod
    def glStencilOpSeparate(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @overload
    @staticmethod
    def glTexParameterfv(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glTexParameterfv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def glTexParameteri(p0: int, p1: int, p2: int) -> None: ...
    @overload
    @staticmethod
    def glTexParameteriv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glTexParameteriv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def glUniform1f(p0: int, p1: float) -> None: ...
    @overload
    @staticmethod
    def glUniform1fv(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniform1fv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def glUniform1i(p0: int, p1: int) -> None: ...
    @overload
    @staticmethod
    def glUniform1iv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniform1iv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def glUniform2f(p0: int, p1: float, p2: float) -> None: ...
    @overload
    @staticmethod
    def glUniform2fv(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniform2fv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def glUniform2i(p0: int, p1: int, p2: int) -> None: ...
    @overload
    @staticmethod
    def glUniform2iv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glUniform2iv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @staticmethod
    def glUniform3f(p0: int, p1: float, p2: float, p3: float) -> None: ...
    @overload
    @staticmethod
    def glUniform3fv(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniform3fv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def glUniform3i(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @overload
    @staticmethod
    def glUniform3iv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniform3iv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def glUniform4f(p0: int, p1: float, p2: float, p3: float, p4: float) -> None: ...
    @overload
    @staticmethod
    def glUniform4fv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glUniform4fv(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @staticmethod
    def glUniform4i(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @overload
    @staticmethod
    def glUniform4iv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glUniform4iv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix2fv(p0: int, p1: int, p2: bool, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix2fv(p0: int, p1: int, p2: bool, p3: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix3fv(p0: int, p1: int, p2: bool, p3: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix3fv(p0: int, p1: int, p2: bool, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix4fv(p0: int, p1: int, p2: bool, p3: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glUniformMatrix4fv(p0: int, p1: int, p2: bool, p3: Any, p4: int) -> None: ...
    @staticmethod
    def glUseProgram(p0: int) -> None: ...
    @staticmethod
    def glValidateProgram(p0: int) -> None: ...
    @staticmethod
    def glVertexAttrib1f(p0: int, p1: float) -> None: ...
    @overload
    @staticmethod
    def glVertexAttrib1fv(p0: int, p1: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glVertexAttrib1fv(p0: int, p1: Any, p2: int) -> None: ...
    @staticmethod
    def glVertexAttrib2f(p0: int, p1: float, p2: float) -> None: ...
    @overload
    @staticmethod
    def glVertexAttrib2fv(p0: int, p1: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glVertexAttrib2fv(p0: int, p1: Any, p2: int) -> None: ...
    @staticmethod
    def glVertexAttrib3f(p0: int, p1: float, p2: float, p3: float) -> None: ...
    @overload
    @staticmethod
    def glVertexAttrib3fv(p0: int, p1: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glVertexAttrib3fv(p0: int, p1: Any, p2: int) -> None: ...
    @staticmethod
    def glVertexAttrib4f(p0: int, p1: float, p2: float, p3: float, p4: float) -> None: ...
    @overload
    @staticmethod
    def glVertexAttrib4fv(p0: int, p1: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glVertexAttrib4fv(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glVertexAttribPointer(p0: int, p1: int, p2: int, p3: bool, p4: int, p5: int) -> None: ...
    @overload
    @staticmethod
    def glVertexAttribPointer(p0: int, p1: int, p2: int, p3: bool, p4: int, p5: Buffer) -> None: ...
    @staticmethod
    def glHint(p0: int, p1: int) -> None: ...
    @staticmethod
    def glActiveTexture(p0: int) -> None: ...
    @staticmethod
    def glBindTexture(p0: int, p1: int) -> None: ...
    @staticmethod
    def glBlendFunc(p0: int, p1: int) -> None: ...
    @staticmethod
    def glClear(p0: int) -> None: ...
    @staticmethod
    def glClearColor(p0: float, p1: float, p2: float, p3: float) -> None: ...
    @staticmethod
    def glClearDepthf(p0: float) -> None: ...
    @staticmethod
    def glClearStencil(p0: int) -> None: ...
    @staticmethod
    def glColorMask(p0: bool, p1: bool, p2: bool, p3: bool) -> None: ...
    @staticmethod
    def glCompressedTexImage2D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: Buffer) -> None: ...
    @staticmethod
    def glCompressedTexSubImage2D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: Buffer) -> None: ...
    @staticmethod
    def glCopyTexImage2D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int) -> None: ...
    @staticmethod
    def glCopyTexSubImage2D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int) -> None: ...
    @staticmethod
    def glCullFace(p0: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteTextures(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glDeleteTextures(p0: int, p1: Any, p2: int) -> None: ...
    @staticmethod
    def glDepthFunc(p0: int) -> None: ...
    @staticmethod
    def glDepthMask(p0: bool) -> None: ...
    @staticmethod
    def glDepthRangef(p0: float, p1: float) -> None: ...
    @staticmethod
    def glDisable(p0: int) -> None: ...
    @staticmethod
    def glDrawArrays(p0: int, p1: int, p2: int) -> None: ...
    @overload
    @staticmethod
    def glDrawElements(p0: int, p1: int, p2: int, p3: Buffer) -> None: ...
    @overload
    @staticmethod
    def glDrawElements(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glEnable(p0: int) -> None: ...
    @staticmethod
    def glFinish() -> None: ...
    @staticmethod
    def glFlush() -> None: ...
    @staticmethod
    def glFrontFace(p0: int) -> None: ...
    @overload
    @staticmethod
    def glGenTextures(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGenTextures(p0: int, p1: Any, p2: int) -> None: ...
    @staticmethod
    def glGetError() -> int: ...
    @overload
    @staticmethod
    def glGetIntegerv(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetIntegerv(p0: int, p1: Any, p2: int) -> None: ...
    @staticmethod
    def glGetString(p0: int) -> str: ...
    @staticmethod
    def glLineWidth(p0: float) -> None: ...
    @staticmethod
    def glPixelStorei(p0: int, p1: int) -> None: ...
    @staticmethod
    def glPolygonOffset(p0: float, p1: float) -> None: ...
    @staticmethod
    def glReadPixels(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: Buffer) -> None: ...
    @staticmethod
    def glSampleCoverage(p0: float, p1: bool) -> None: ...
    @staticmethod
    def glScissor(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glStencilFunc(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glStencilMask(p0: int) -> None: ...
    @staticmethod
    def glStencilOp(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glTexImage2D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: Buffer) -> None: ...
    @staticmethod
    def glTexParameterf(p0: int, p1: int, p2: float) -> None: ...
    @staticmethod
    def glTexSubImage2D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: Buffer) -> None: ...
    @staticmethod
    def glViewport(p0: int, p1: int, p2: int, p3: int) -> None: ...

from typing import Any, ClassVar, overload
from java.nio.FloatBuffer import FloatBuffer
from java.nio.IntBuffer import IntBuffer

class GLES31:
    GL_ACTIVE_ATOMIC_COUNTER_BUFFERS: ClassVar[int]
    GL_ACTIVE_PROGRAM: ClassVar[int]
    GL_ACTIVE_RESOURCES: ClassVar[int]
    GL_ACTIVE_VARIABLES: ClassVar[int]
    GL_ALL_BARRIER_BITS: ClassVar[int]
    GL_ALL_SHADER_BITS: ClassVar[int]
    GL_ARRAY_SIZE: ClassVar[int]
    GL_ARRAY_STRIDE: ClassVar[int]
    GL_ATOMIC_COUNTER_BARRIER_BIT: ClassVar[int]
    GL_ATOMIC_COUNTER_BUFFER: ClassVar[int]
    GL_ATOMIC_COUNTER_BUFFER_BINDING: ClassVar[int]
    GL_ATOMIC_COUNTER_BUFFER_INDEX: ClassVar[int]
    GL_ATOMIC_COUNTER_BUFFER_SIZE: ClassVar[int]
    GL_ATOMIC_COUNTER_BUFFER_START: ClassVar[int]
    GL_BLOCK_INDEX: ClassVar[int]
    GL_BUFFER_BINDING: ClassVar[int]
    GL_BUFFER_DATA_SIZE: ClassVar[int]
    GL_BUFFER_UPDATE_BARRIER_BIT: ClassVar[int]
    GL_BUFFER_VARIABLE: ClassVar[int]
    GL_COMMAND_BARRIER_BIT: ClassVar[int]
    GL_COMPUTE_SHADER: ClassVar[int]
    GL_COMPUTE_SHADER_BIT: ClassVar[int]
    GL_COMPUTE_WORK_GROUP_SIZE: ClassVar[int]
    GL_DEPTH_STENCIL_TEXTURE_MODE: ClassVar[int]
    GL_DISPATCH_INDIRECT_BUFFER: ClassVar[int]
    GL_DISPATCH_INDIRECT_BUFFER_BINDING: ClassVar[int]
    GL_DRAW_INDIRECT_BUFFER: ClassVar[int]
    GL_DRAW_INDIRECT_BUFFER_BINDING: ClassVar[int]
    GL_ELEMENT_ARRAY_BARRIER_BIT: ClassVar[int]
    GL_FRAGMENT_SHADER_BIT: ClassVar[int]
    GL_FRAMEBUFFER_BARRIER_BIT: ClassVar[int]
    GL_FRAMEBUFFER_DEFAULT_FIXED_SAMPLE_LOCATIONS: ClassVar[int]
    GL_FRAMEBUFFER_DEFAULT_HEIGHT: ClassVar[int]
    GL_FRAMEBUFFER_DEFAULT_SAMPLES: ClassVar[int]
    GL_FRAMEBUFFER_DEFAULT_WIDTH: ClassVar[int]
    GL_IMAGE_2D: ClassVar[int]
    GL_IMAGE_2D_ARRAY: ClassVar[int]
    GL_IMAGE_3D: ClassVar[int]
    GL_IMAGE_BINDING_ACCESS: ClassVar[int]
    GL_IMAGE_BINDING_FORMAT: ClassVar[int]
    GL_IMAGE_BINDING_LAYER: ClassVar[int]
    GL_IMAGE_BINDING_LAYERED: ClassVar[int]
    GL_IMAGE_BINDING_LEVEL: ClassVar[int]
    GL_IMAGE_BINDING_NAME: ClassVar[int]
    GL_IMAGE_CUBE: ClassVar[int]
    GL_IMAGE_FORMAT_COMPATIBILITY_BY_CLASS: ClassVar[int]
    GL_IMAGE_FORMAT_COMPATIBILITY_BY_SIZE: ClassVar[int]
    GL_IMAGE_FORMAT_COMPATIBILITY_TYPE: ClassVar[int]
    GL_INT_IMAGE_2D: ClassVar[int]
    GL_INT_IMAGE_2D_ARRAY: ClassVar[int]
    GL_INT_IMAGE_3D: ClassVar[int]
    GL_INT_IMAGE_CUBE: ClassVar[int]
    GL_INT_SAMPLER_2D_MULTISAMPLE: ClassVar[int]
    GL_IS_ROW_MAJOR: ClassVar[int]
    GL_LOCATION: ClassVar[int]
    GL_MATRIX_STRIDE: ClassVar[int]
    GL_MAX_ATOMIC_COUNTER_BUFFER_BINDINGS: ClassVar[int]
    GL_MAX_ATOMIC_COUNTER_BUFFER_SIZE: ClassVar[int]
    GL_MAX_COLOR_TEXTURE_SAMPLES: ClassVar[int]
    GL_MAX_COMBINED_ATOMIC_COUNTERS: ClassVar[int]
    GL_MAX_COMBINED_ATOMIC_COUNTER_BUFFERS: ClassVar[int]
    GL_MAX_COMBINED_COMPUTE_UNIFORM_COMPONENTS: ClassVar[int]
    GL_MAX_COMBINED_IMAGE_UNIFORMS: ClassVar[int]
    GL_MAX_COMBINED_SHADER_OUTPUT_RESOURCES: ClassVar[int]
    GL_MAX_COMBINED_SHADER_STORAGE_BLOCKS: ClassVar[int]
    GL_MAX_COMPUTE_ATOMIC_COUNTERS: ClassVar[int]
    GL_MAX_COMPUTE_ATOMIC_COUNTER_BUFFERS: ClassVar[int]
    GL_MAX_COMPUTE_IMAGE_UNIFORMS: ClassVar[int]
    GL_MAX_COMPUTE_SHADER_STORAGE_BLOCKS: ClassVar[int]
    GL_MAX_COMPUTE_SHARED_MEMORY_SIZE: ClassVar[int]
    GL_MAX_COMPUTE_TEXTURE_IMAGE_UNITS: ClassVar[int]
    GL_MAX_COMPUTE_UNIFORM_BLOCKS: ClassVar[int]
    GL_MAX_COMPUTE_UNIFORM_COMPONENTS: ClassVar[int]
    GL_MAX_COMPUTE_WORK_GROUP_COUNT: ClassVar[int]
    GL_MAX_COMPUTE_WORK_GROUP_INVOCATIONS: ClassVar[int]
    GL_MAX_COMPUTE_WORK_GROUP_SIZE: ClassVar[int]
    GL_MAX_DEPTH_TEXTURE_SAMPLES: ClassVar[int]
    GL_MAX_FRAGMENT_ATOMIC_COUNTERS: ClassVar[int]
    GL_MAX_FRAGMENT_ATOMIC_COUNTER_BUFFERS: ClassVar[int]
    GL_MAX_FRAGMENT_IMAGE_UNIFORMS: ClassVar[int]
    GL_MAX_FRAGMENT_SHADER_STORAGE_BLOCKS: ClassVar[int]
    GL_MAX_FRAMEBUFFER_HEIGHT: ClassVar[int]
    GL_MAX_FRAMEBUFFER_SAMPLES: ClassVar[int]
    GL_MAX_FRAMEBUFFER_WIDTH: ClassVar[int]
    GL_MAX_IMAGE_UNITS: ClassVar[int]
    GL_MAX_INTEGER_SAMPLES: ClassVar[int]
    GL_MAX_NAME_LENGTH: ClassVar[int]
    GL_MAX_NUM_ACTIVE_VARIABLES: ClassVar[int]
    GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET: ClassVar[int]
    GL_MAX_SAMPLE_MASK_WORDS: ClassVar[int]
    GL_MAX_SHADER_STORAGE_BLOCK_SIZE: ClassVar[int]
    GL_MAX_SHADER_STORAGE_BUFFER_BINDINGS: ClassVar[int]
    GL_MAX_UNIFORM_LOCATIONS: ClassVar[int]
    GL_MAX_VERTEX_ATOMIC_COUNTERS: ClassVar[int]
    GL_MAX_VERTEX_ATOMIC_COUNTER_BUFFERS: ClassVar[int]
    GL_MAX_VERTEX_ATTRIB_BINDINGS: ClassVar[int]
    GL_MAX_VERTEX_ATTRIB_RELATIVE_OFFSET: ClassVar[int]
    GL_MAX_VERTEX_ATTRIB_STRIDE: ClassVar[int]
    GL_MAX_VERTEX_IMAGE_UNIFORMS: ClassVar[int]
    GL_MAX_VERTEX_SHADER_STORAGE_BLOCKS: ClassVar[int]
    GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET: ClassVar[int]
    GL_NAME_LENGTH: ClassVar[int]
    GL_NUM_ACTIVE_VARIABLES: ClassVar[int]
    GL_OFFSET: ClassVar[int]
    GL_PIXEL_BUFFER_BARRIER_BIT: ClassVar[int]
    GL_PROGRAM_INPUT: ClassVar[int]
    GL_PROGRAM_OUTPUT: ClassVar[int]
    GL_PROGRAM_PIPELINE_BINDING: ClassVar[int]
    GL_PROGRAM_SEPARABLE: ClassVar[int]
    GL_READ_ONLY: ClassVar[int]
    GL_READ_WRITE: ClassVar[int]
    GL_REFERENCED_BY_COMPUTE_SHADER: ClassVar[int]
    GL_REFERENCED_BY_FRAGMENT_SHADER: ClassVar[int]
    GL_REFERENCED_BY_VERTEX_SHADER: ClassVar[int]
    GL_SAMPLER_2D_MULTISAMPLE: ClassVar[int]
    GL_SAMPLE_MASK: ClassVar[int]
    GL_SAMPLE_MASK_VALUE: ClassVar[int]
    GL_SAMPLE_POSITION: ClassVar[int]
    GL_SHADER_IMAGE_ACCESS_BARRIER_BIT: ClassVar[int]
    GL_SHADER_STORAGE_BARRIER_BIT: ClassVar[int]
    GL_SHADER_STORAGE_BLOCK: ClassVar[int]
    GL_SHADER_STORAGE_BUFFER: ClassVar[int]
    GL_SHADER_STORAGE_BUFFER_BINDING: ClassVar[int]
    GL_SHADER_STORAGE_BUFFER_OFFSET_ALIGNMENT: ClassVar[int]
    GL_SHADER_STORAGE_BUFFER_SIZE: ClassVar[int]
    GL_SHADER_STORAGE_BUFFER_START: ClassVar[int]
    GL_STENCIL_INDEX: ClassVar[int]
    GL_TEXTURE_2D_MULTISAMPLE: ClassVar[int]
    GL_TEXTURE_ALPHA_SIZE: ClassVar[int]
    GL_TEXTURE_ALPHA_TYPE: ClassVar[int]
    GL_TEXTURE_BINDING_2D_MULTISAMPLE: ClassVar[int]
    GL_TEXTURE_BLUE_SIZE: ClassVar[int]
    GL_TEXTURE_BLUE_TYPE: ClassVar[int]
    GL_TEXTURE_COMPRESSED: ClassVar[int]
    GL_TEXTURE_DEPTH: ClassVar[int]
    GL_TEXTURE_DEPTH_SIZE: ClassVar[int]
    GL_TEXTURE_DEPTH_TYPE: ClassVar[int]
    GL_TEXTURE_FETCH_BARRIER_BIT: ClassVar[int]
    GL_TEXTURE_FIXED_SAMPLE_LOCATIONS: ClassVar[int]
    GL_TEXTURE_GREEN_SIZE: ClassVar[int]
    GL_TEXTURE_GREEN_TYPE: ClassVar[int]
    GL_TEXTURE_HEIGHT: ClassVar[int]
    GL_TEXTURE_INTERNAL_FORMAT: ClassVar[int]
    GL_TEXTURE_RED_SIZE: ClassVar[int]
    GL_TEXTURE_RED_TYPE: ClassVar[int]
    GL_TEXTURE_SAMPLES: ClassVar[int]
    GL_TEXTURE_SHARED_SIZE: ClassVar[int]
    GL_TEXTURE_STENCIL_SIZE: ClassVar[int]
    GL_TEXTURE_UPDATE_BARRIER_BIT: ClassVar[int]
    GL_TEXTURE_WIDTH: ClassVar[int]
    GL_TOP_LEVEL_ARRAY_SIZE: ClassVar[int]
    GL_TOP_LEVEL_ARRAY_STRIDE: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_BARRIER_BIT: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_VARYING: ClassVar[int]
    GL_TYPE: ClassVar[int]
    GL_UNIFORM: ClassVar[int]
    GL_UNIFORM_BARRIER_BIT: ClassVar[int]
    GL_UNIFORM_BLOCK: ClassVar[int]
    GL_UNSIGNED_INT_ATOMIC_COUNTER: ClassVar[int]
    GL_UNSIGNED_INT_IMAGE_2D: ClassVar[int]
    GL_UNSIGNED_INT_IMAGE_2D_ARRAY: ClassVar[int]
    GL_UNSIGNED_INT_IMAGE_3D: ClassVar[int]
    GL_UNSIGNED_INT_IMAGE_CUBE: ClassVar[int]
    GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_BARRIER_BIT: ClassVar[int]
    GL_VERTEX_ATTRIB_BINDING: ClassVar[int]
    GL_VERTEX_ATTRIB_RELATIVE_OFFSET: ClassVar[int]
    GL_VERTEX_BINDING_BUFFER: ClassVar[int]
    GL_VERTEX_BINDING_DIVISOR: ClassVar[int]
    GL_VERTEX_BINDING_OFFSET: ClassVar[int]
    GL_VERTEX_BINDING_STRIDE: ClassVar[int]
    GL_VERTEX_SHADER_BIT: ClassVar[int]
    GL_WRITE_ONLY: ClassVar[int]
    GL_ACTIVE_UNIFORM_BLOCKS: ClassVar[int]
    GL_ACTIVE_UNIFORM_BLOCK_MAX_NAME_LENGTH: ClassVar[int]
    GL_ALREADY_SIGNALED: ClassVar[int]
    GL_ANY_SAMPLES_PASSED: ClassVar[int]
    GL_ANY_SAMPLES_PASSED_CONSERVATIVE: ClassVar[int]
    GL_BLUE: ClassVar[int]
    GL_BUFFER_ACCESS_FLAGS: ClassVar[int]
    GL_BUFFER_MAPPED: ClassVar[int]
    GL_BUFFER_MAP_LENGTH: ClassVar[int]
    GL_BUFFER_MAP_OFFSET: ClassVar[int]
    GL_BUFFER_MAP_POINTER: ClassVar[int]
    GL_COLOR: ClassVar[int]
    GL_COLOR_ATTACHMENT1: ClassVar[int]
    GL_COLOR_ATTACHMENT10: ClassVar[int]
    GL_COLOR_ATTACHMENT11: ClassVar[int]
    GL_COLOR_ATTACHMENT12: ClassVar[int]
    GL_COLOR_ATTACHMENT13: ClassVar[int]
    GL_COLOR_ATTACHMENT14: ClassVar[int]
    GL_COLOR_ATTACHMENT15: ClassVar[int]
    GL_COLOR_ATTACHMENT2: ClassVar[int]
    GL_COLOR_ATTACHMENT3: ClassVar[int]
    GL_COLOR_ATTACHMENT4: ClassVar[int]
    GL_COLOR_ATTACHMENT5: ClassVar[int]
    GL_COLOR_ATTACHMENT6: ClassVar[int]
    GL_COLOR_ATTACHMENT7: ClassVar[int]
    GL_COLOR_ATTACHMENT8: ClassVar[int]
    GL_COLOR_ATTACHMENT9: ClassVar[int]
    GL_COMPARE_REF_TO_TEXTURE: ClassVar[int]
    GL_COMPRESSED_R11_EAC: ClassVar[int]
    GL_COMPRESSED_RG11_EAC: ClassVar[int]
    GL_COMPRESSED_RGB8_ETC2: ClassVar[int]
    GL_COMPRESSED_RGB8_PUNCHTHROUGH_ALPHA1_ETC2: ClassVar[int]
    GL_COMPRESSED_RGBA8_ETC2_EAC: ClassVar[int]
    GL_COMPRESSED_SIGNED_R11_EAC: ClassVar[int]
    GL_COMPRESSED_SIGNED_RG11_EAC: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ETC2_EAC: ClassVar[int]
    GL_COMPRESSED_SRGB8_ETC2: ClassVar[int]
    GL_COMPRESSED_SRGB8_PUNCHTHROUGH_ALPHA1_ETC2: ClassVar[int]
    GL_CONDITION_SATISFIED: ClassVar[int]
    GL_COPY_READ_BUFFER: ClassVar[int]
    GL_COPY_READ_BUFFER_BINDING: ClassVar[int]
    GL_COPY_WRITE_BUFFER: ClassVar[int]
    GL_COPY_WRITE_BUFFER_BINDING: ClassVar[int]
    GL_CURRENT_QUERY: ClassVar[int]
    GL_DEPTH: ClassVar[int]
    GL_DEPTH24_STENCIL8: ClassVar[int]
    GL_DEPTH32F_STENCIL8: ClassVar[int]
    GL_DEPTH_COMPONENT24: ClassVar[int]
    GL_DEPTH_COMPONENT32F: ClassVar[int]
    GL_DEPTH_STENCIL: ClassVar[int]
    GL_DEPTH_STENCIL_ATTACHMENT: ClassVar[int]
    GL_DRAW_BUFFER0: ClassVar[int]
    GL_DRAW_BUFFER1: ClassVar[int]
    GL_DRAW_BUFFER10: ClassVar[int]
    GL_DRAW_BUFFER11: ClassVar[int]
    GL_DRAW_BUFFER12: ClassVar[int]
    GL_DRAW_BUFFER13: ClassVar[int]
    GL_DRAW_BUFFER14: ClassVar[int]
    GL_DRAW_BUFFER15: ClassVar[int]
    GL_DRAW_BUFFER2: ClassVar[int]
    GL_DRAW_BUFFER3: ClassVar[int]
    GL_DRAW_BUFFER4: ClassVar[int]
    GL_DRAW_BUFFER5: ClassVar[int]
    GL_DRAW_BUFFER6: ClassVar[int]
    GL_DRAW_BUFFER7: ClassVar[int]
    GL_DRAW_BUFFER8: ClassVar[int]
    GL_DRAW_BUFFER9: ClassVar[int]
    GL_DRAW_FRAMEBUFFER: ClassVar[int]
    GL_DRAW_FRAMEBUFFER_BINDING: ClassVar[int]
    GL_DYNAMIC_COPY: ClassVar[int]
    GL_DYNAMIC_READ: ClassVar[int]
    GL_FLOAT_32_UNSIGNED_INT_24_8_REV: ClassVar[int]
    GL_FLOAT_MAT2x3: ClassVar[int]
    GL_FLOAT_MAT2x4: ClassVar[int]
    GL_FLOAT_MAT3x2: ClassVar[int]
    GL_FLOAT_MAT3x4: ClassVar[int]
    GL_FLOAT_MAT4x2: ClassVar[int]
    GL_FLOAT_MAT4x3: ClassVar[int]
    GL_FRAGMENT_SHADER_DERIVATIVE_HINT: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_ALPHA_SIZE: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_BLUE_SIZE: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_DEPTH_SIZE: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_GREEN_SIZE: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_RED_SIZE: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_STENCIL_SIZE: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER: ClassVar[int]
    GL_FRAMEBUFFER_DEFAULT: ClassVar[int]
    GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE: ClassVar[int]
    GL_FRAMEBUFFER_UNDEFINED: ClassVar[int]
    GL_GREEN: ClassVar[int]
    GL_HALF_FLOAT: ClassVar[int]
    GL_INTERLEAVED_ATTRIBS: ClassVar[int]
    GL_INT_2_10_10_10_REV: ClassVar[int]
    GL_INT_SAMPLER_2D: ClassVar[int]
    GL_INT_SAMPLER_2D_ARRAY: ClassVar[int]
    GL_INT_SAMPLER_3D: ClassVar[int]
    GL_INT_SAMPLER_CUBE: ClassVar[int]
    GL_INVALID_INDEX: ClassVar[int]
    GL_MAJOR_VERSION: ClassVar[int]
    GL_MAP_FLUSH_EXPLICIT_BIT: ClassVar[int]
    GL_MAP_INVALIDATE_BUFFER_BIT: ClassVar[int]
    GL_MAP_INVALIDATE_RANGE_BIT: ClassVar[int]
    GL_MAP_READ_BIT: ClassVar[int]
    GL_MAP_UNSYNCHRONIZED_BIT: ClassVar[int]
    GL_MAP_WRITE_BIT: ClassVar[int]
    GL_MAX: ClassVar[int]
    GL_MAX_3D_TEXTURE_SIZE: ClassVar[int]
    GL_MAX_ARRAY_TEXTURE_LAYERS: ClassVar[int]
    GL_MAX_COLOR_ATTACHMENTS: ClassVar[int]
    GL_MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS: ClassVar[int]
    GL_MAX_COMBINED_UNIFORM_BLOCKS: ClassVar[int]
    GL_MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS: ClassVar[int]
    GL_MAX_DRAW_BUFFERS: ClassVar[int]
    GL_MAX_ELEMENTS_INDICES: ClassVar[int]
    GL_MAX_ELEMENTS_VERTICES: ClassVar[int]
    GL_MAX_ELEMENT_INDEX: ClassVar[int]
    GL_MAX_FRAGMENT_INPUT_COMPONENTS: ClassVar[int]
    GL_MAX_FRAGMENT_UNIFORM_BLOCKS: ClassVar[int]
    GL_MAX_FRAGMENT_UNIFORM_COMPONENTS: ClassVar[int]
    GL_MAX_PROGRAM_TEXEL_OFFSET: ClassVar[int]
    GL_MAX_SAMPLES: ClassVar[int]
    GL_MAX_SERVER_WAIT_TIMEOUT: ClassVar[int]
    GL_MAX_TEXTURE_LOD_BIAS: ClassVar[int]
    GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS: ClassVar[int]
    GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS: ClassVar[int]
    GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS: ClassVar[int]
    GL_MAX_UNIFORM_BLOCK_SIZE: ClassVar[int]
    GL_MAX_UNIFORM_BUFFER_BINDINGS: ClassVar[int]
    GL_MAX_VARYING_COMPONENTS: ClassVar[int]
    GL_MAX_VERTEX_OUTPUT_COMPONENTS: ClassVar[int]
    GL_MAX_VERTEX_UNIFORM_BLOCKS: ClassVar[int]
    GL_MAX_VERTEX_UNIFORM_COMPONENTS: ClassVar[int]
    GL_MIN: ClassVar[int]
    GL_MINOR_VERSION: ClassVar[int]
    GL_MIN_PROGRAM_TEXEL_OFFSET: ClassVar[int]
    GL_NUM_EXTENSIONS: ClassVar[int]
    GL_NUM_PROGRAM_BINARY_FORMATS: ClassVar[int]
    GL_NUM_SAMPLE_COUNTS: ClassVar[int]
    GL_OBJECT_TYPE: ClassVar[int]
    GL_PACK_ROW_LENGTH: ClassVar[int]
    GL_PACK_SKIP_PIXELS: ClassVar[int]
    GL_PACK_SKIP_ROWS: ClassVar[int]
    GL_PIXEL_PACK_BUFFER: ClassVar[int]
    GL_PIXEL_PACK_BUFFER_BINDING: ClassVar[int]
    GL_PIXEL_UNPACK_BUFFER: ClassVar[int]
    GL_PIXEL_UNPACK_BUFFER_BINDING: ClassVar[int]
    GL_PRIMITIVE_RESTART_FIXED_INDEX: ClassVar[int]
    GL_PROGRAM_BINARY_FORMATS: ClassVar[int]
    GL_PROGRAM_BINARY_LENGTH: ClassVar[int]
    GL_PROGRAM_BINARY_RETRIEVABLE_HINT: ClassVar[int]
    GL_QUERY_RESULT: ClassVar[int]
    GL_QUERY_RESULT_AVAILABLE: ClassVar[int]
    GL_R11F_G11F_B10F: ClassVar[int]
    GL_R16F: ClassVar[int]
    GL_R16I: ClassVar[int]
    GL_R16UI: ClassVar[int]
    GL_R32F: ClassVar[int]
    GL_R32I: ClassVar[int]
    GL_R32UI: ClassVar[int]
    GL_R8: ClassVar[int]
    GL_R8I: ClassVar[int]
    GL_R8UI: ClassVar[int]
    GL_R8_SNORM: ClassVar[int]
    GL_RASTERIZER_DISCARD: ClassVar[int]
    GL_READ_BUFFER: ClassVar[int]
    GL_READ_FRAMEBUFFER: ClassVar[int]
    GL_READ_FRAMEBUFFER_BINDING: ClassVar[int]
    GL_RED: ClassVar[int]
    GL_RED_INTEGER: ClassVar[int]
    GL_RENDERBUFFER_SAMPLES: ClassVar[int]
    GL_RG: ClassVar[int]
    GL_RG16F: ClassVar[int]
    GL_RG16I: ClassVar[int]
    GL_RG16UI: ClassVar[int]
    GL_RG32F: ClassVar[int]
    GL_RG32I: ClassVar[int]
    GL_RG32UI: ClassVar[int]
    GL_RG8: ClassVar[int]
    GL_RG8I: ClassVar[int]
    GL_RG8UI: ClassVar[int]
    GL_RG8_SNORM: ClassVar[int]
    GL_RGB10_A2: ClassVar[int]
    GL_RGB10_A2UI: ClassVar[int]
    GL_RGB16F: ClassVar[int]
    GL_RGB16I: ClassVar[int]
    GL_RGB16UI: ClassVar[int]
    GL_RGB32F: ClassVar[int]
    GL_RGB32I: ClassVar[int]
    GL_RGB32UI: ClassVar[int]
    GL_RGB8: ClassVar[int]
    GL_RGB8I: ClassVar[int]
    GL_RGB8UI: ClassVar[int]
    GL_RGB8_SNORM: ClassVar[int]
    GL_RGB9_E5: ClassVar[int]
    GL_RGBA16F: ClassVar[int]
    GL_RGBA16I: ClassVar[int]
    GL_RGBA16UI: ClassVar[int]
    GL_RGBA32F: ClassVar[int]
    GL_RGBA32I: ClassVar[int]
    GL_RGBA32UI: ClassVar[int]
    GL_RGBA8: ClassVar[int]
    GL_RGBA8I: ClassVar[int]
    GL_RGBA8UI: ClassVar[int]
    GL_RGBA8_SNORM: ClassVar[int]
    GL_RGBA_INTEGER: ClassVar[int]
    GL_RGB_INTEGER: ClassVar[int]
    GL_RG_INTEGER: ClassVar[int]
    GL_SAMPLER_2D_ARRAY: ClassVar[int]
    GL_SAMPLER_2D_ARRAY_SHADOW: ClassVar[int]
    GL_SAMPLER_2D_SHADOW: ClassVar[int]
    GL_SAMPLER_3D: ClassVar[int]
    GL_SAMPLER_BINDING: ClassVar[int]
    GL_SAMPLER_CUBE_SHADOW: ClassVar[int]
    GL_SEPARATE_ATTRIBS: ClassVar[int]
    GL_SIGNALED: ClassVar[int]
    GL_SIGNED_NORMALIZED: ClassVar[int]
    GL_SRGB: ClassVar[int]
    GL_SRGB8: ClassVar[int]
    GL_SRGB8_ALPHA8: ClassVar[int]
    GL_STATIC_COPY: ClassVar[int]
    GL_STATIC_READ: ClassVar[int]
    GL_STENCIL: ClassVar[int]
    GL_STREAM_COPY: ClassVar[int]
    GL_STREAM_READ: ClassVar[int]
    GL_SYNC_CONDITION: ClassVar[int]
    GL_SYNC_FENCE: ClassVar[int]
    GL_SYNC_FLAGS: ClassVar[int]
    GL_SYNC_FLUSH_COMMANDS_BIT: ClassVar[int]
    GL_SYNC_GPU_COMMANDS_COMPLETE: ClassVar[int]
    GL_SYNC_STATUS: ClassVar[int]
    GL_TEXTURE_2D_ARRAY: ClassVar[int]
    GL_TEXTURE_3D: ClassVar[int]
    GL_TEXTURE_BASE_LEVEL: ClassVar[int]
    GL_TEXTURE_BINDING_2D_ARRAY: ClassVar[int]
    GL_TEXTURE_BINDING_3D: ClassVar[int]
    GL_TEXTURE_COMPARE_FUNC: ClassVar[int]
    GL_TEXTURE_COMPARE_MODE: ClassVar[int]
    GL_TEXTURE_IMMUTABLE_FORMAT: ClassVar[int]
    GL_TEXTURE_IMMUTABLE_LEVELS: ClassVar[int]
    GL_TEXTURE_MAX_LEVEL: ClassVar[int]
    GL_TEXTURE_MAX_LOD: ClassVar[int]
    GL_TEXTURE_MIN_LOD: ClassVar[int]
    GL_TEXTURE_SWIZZLE_A: ClassVar[int]
    GL_TEXTURE_SWIZZLE_B: ClassVar[int]
    GL_TEXTURE_SWIZZLE_G: ClassVar[int]
    GL_TEXTURE_SWIZZLE_R: ClassVar[int]
    GL_TEXTURE_WRAP_R: ClassVar[int]
    GL_TIMEOUT_EXPIRED: ClassVar[int]
    GL_TIMEOUT_IGNORED: ClassVar[int]
    GL_TRANSFORM_FEEDBACK: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_ACTIVE: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_BINDING: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_BUFFER: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_BUFFER_BINDING: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_BUFFER_MODE: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_BUFFER_SIZE: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_BUFFER_START: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_PAUSED: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_VARYINGS: ClassVar[int]
    GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH: ClassVar[int]
    GL_UNIFORM_ARRAY_STRIDE: ClassVar[int]
    GL_UNIFORM_BLOCK_ACTIVE_UNIFORMS: ClassVar[int]
    GL_UNIFORM_BLOCK_ACTIVE_UNIFORM_INDICES: ClassVar[int]
    GL_UNIFORM_BLOCK_BINDING: ClassVar[int]
    GL_UNIFORM_BLOCK_DATA_SIZE: ClassVar[int]
    GL_UNIFORM_BLOCK_INDEX: ClassVar[int]
    GL_UNIFORM_BLOCK_NAME_LENGTH: ClassVar[int]
    GL_UNIFORM_BLOCK_REFERENCED_BY_FRAGMENT_SHADER: ClassVar[int]
    GL_UNIFORM_BLOCK_REFERENCED_BY_VERTEX_SHADER: ClassVar[int]
    GL_UNIFORM_BUFFER: ClassVar[int]
    GL_UNIFORM_BUFFER_BINDING: ClassVar[int]
    GL_UNIFORM_BUFFER_OFFSET_ALIGNMENT: ClassVar[int]
    GL_UNIFORM_BUFFER_SIZE: ClassVar[int]
    GL_UNIFORM_BUFFER_START: ClassVar[int]
    GL_UNIFORM_IS_ROW_MAJOR: ClassVar[int]
    GL_UNIFORM_MATRIX_STRIDE: ClassVar[int]
    GL_UNIFORM_NAME_LENGTH: ClassVar[int]
    GL_UNIFORM_OFFSET: ClassVar[int]
    GL_UNIFORM_SIZE: ClassVar[int]
    GL_UNIFORM_TYPE: ClassVar[int]
    GL_UNPACK_IMAGE_HEIGHT: ClassVar[int]
    GL_UNPACK_ROW_LENGTH: ClassVar[int]
    GL_UNPACK_SKIP_IMAGES: ClassVar[int]
    GL_UNPACK_SKIP_PIXELS: ClassVar[int]
    GL_UNPACK_SKIP_ROWS: ClassVar[int]
    GL_UNSIGNALED: ClassVar[int]
    GL_UNSIGNED_INT_10F_11F_11F_REV: ClassVar[int]
    GL_UNSIGNED_INT_24_8: ClassVar[int]
    GL_UNSIGNED_INT_2_10_10_10_REV: ClassVar[int]
    GL_UNSIGNED_INT_5_9_9_9_REV: ClassVar[int]
    GL_UNSIGNED_INT_SAMPLER_2D: ClassVar[int]
    GL_UNSIGNED_INT_SAMPLER_2D_ARRAY: ClassVar[int]
    GL_UNSIGNED_INT_SAMPLER_3D: ClassVar[int]
    GL_UNSIGNED_INT_SAMPLER_CUBE: ClassVar[int]
    GL_UNSIGNED_INT_VEC2: ClassVar[int]
    GL_UNSIGNED_INT_VEC3: ClassVar[int]
    GL_UNSIGNED_INT_VEC4: ClassVar[int]
    GL_UNSIGNED_NORMALIZED: ClassVar[int]
    GL_VERTEX_ARRAY_BINDING: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_DIVISOR: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_INTEGER: ClassVar[int]
    GL_WAIT_FAILED: ClassVar[int]
    GL_ACTIVE_ATTRIBUTES: ClassVar[int]
    GL_ACTIVE_ATTRIBUTE_MAX_LENGTH: ClassVar[int]
    GL_ACTIVE_TEXTURE: ClassVar[int]
    GL_ACTIVE_UNIFORMS: ClassVar[int]
    GL_ACTIVE_UNIFORM_MAX_LENGTH: ClassVar[int]
    GL_ALIASED_LINE_WIDTH_RANGE: ClassVar[int]
    GL_ALIASED_POINT_SIZE_RANGE: ClassVar[int]
    GL_ALPHA: ClassVar[int]
    GL_ALPHA_BITS: ClassVar[int]
    GL_ALWAYS: ClassVar[int]
    GL_ARRAY_BUFFER: ClassVar[int]
    GL_ARRAY_BUFFER_BINDING: ClassVar[int]
    GL_ATTACHED_SHADERS: ClassVar[int]
    GL_BACK: ClassVar[int]
    GL_BLEND: ClassVar[int]
    GL_BLEND_COLOR: ClassVar[int]
    GL_BLEND_DST_ALPHA: ClassVar[int]
    GL_BLEND_DST_RGB: ClassVar[int]
    GL_BLEND_EQUATION: ClassVar[int]
    GL_BLEND_EQUATION_ALPHA: ClassVar[int]
    GL_BLEND_EQUATION_RGB: ClassVar[int]
    GL_BLEND_SRC_ALPHA: ClassVar[int]
    GL_BLEND_SRC_RGB: ClassVar[int]
    GL_BLUE_BITS: ClassVar[int]
    GL_BOOL: ClassVar[int]
    GL_BOOL_VEC2: ClassVar[int]
    GL_BOOL_VEC3: ClassVar[int]
    GL_BOOL_VEC4: ClassVar[int]
    GL_BUFFER_SIZE: ClassVar[int]
    GL_BUFFER_USAGE: ClassVar[int]
    GL_BYTE: ClassVar[int]
    GL_CCW: ClassVar[int]
    GL_CLAMP_TO_EDGE: ClassVar[int]
    GL_COLOR_ATTACHMENT0: ClassVar[int]
    GL_COLOR_BUFFER_BIT: ClassVar[int]
    GL_COLOR_CLEAR_VALUE: ClassVar[int]
    GL_COLOR_WRITEMASK: ClassVar[int]
    GL_COMPILE_STATUS: ClassVar[int]
    GL_COMPRESSED_TEXTURE_FORMATS: ClassVar[int]
    GL_CONSTANT_ALPHA: ClassVar[int]
    GL_CONSTANT_COLOR: ClassVar[int]
    GL_CULL_FACE: ClassVar[int]
    GL_CULL_FACE_MODE: ClassVar[int]
    GL_CURRENT_PROGRAM: ClassVar[int]
    GL_CURRENT_VERTEX_ATTRIB: ClassVar[int]
    GL_CW: ClassVar[int]
    GL_DECR: ClassVar[int]
    GL_DECR_WRAP: ClassVar[int]
    GL_DELETE_STATUS: ClassVar[int]
    GL_DEPTH_ATTACHMENT: ClassVar[int]
    GL_DEPTH_BITS: ClassVar[int]
    GL_DEPTH_BUFFER_BIT: ClassVar[int]
    GL_DEPTH_CLEAR_VALUE: ClassVar[int]
    GL_DEPTH_COMPONENT: ClassVar[int]
    GL_DEPTH_COMPONENT16: ClassVar[int]
    GL_DEPTH_FUNC: ClassVar[int]
    GL_DEPTH_RANGE: ClassVar[int]
    GL_DEPTH_TEST: ClassVar[int]
    GL_DEPTH_WRITEMASK: ClassVar[int]
    GL_DITHER: ClassVar[int]
    GL_DONT_CARE: ClassVar[int]
    GL_DST_ALPHA: ClassVar[int]
    GL_DST_COLOR: ClassVar[int]
    GL_DYNAMIC_DRAW: ClassVar[int]
    GL_ELEMENT_ARRAY_BUFFER: ClassVar[int]
    GL_ELEMENT_ARRAY_BUFFER_BINDING: ClassVar[int]
    GL_EQUAL: ClassVar[int]
    GL_EXTENSIONS: ClassVar[int]
    GL_FALSE: ClassVar[int]
    GL_FASTEST: ClassVar[int]
    GL_FIXED: ClassVar[int]
    GL_FLOAT: ClassVar[int]
    GL_FLOAT_MAT2: ClassVar[int]
    GL_FLOAT_MAT3: ClassVar[int]
    GL_FLOAT_MAT4: ClassVar[int]
    GL_FLOAT_VEC2: ClassVar[int]
    GL_FLOAT_VEC3: ClassVar[int]
    GL_FLOAT_VEC4: ClassVar[int]
    GL_FRAGMENT_SHADER: ClassVar[int]
    GL_FRAMEBUFFER: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL: ClassVar[int]
    GL_FRAMEBUFFER_BINDING: ClassVar[int]
    GL_FRAMEBUFFER_COMPLETE: ClassVar[int]
    GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT: ClassVar[int]
    GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS: ClassVar[int]
    GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT: ClassVar[int]
    GL_FRAMEBUFFER_UNSUPPORTED: ClassVar[int]
    GL_FRONT: ClassVar[int]
    GL_FRONT_AND_BACK: ClassVar[int]
    GL_FRONT_FACE: ClassVar[int]
    GL_FUNC_ADD: ClassVar[int]
    GL_FUNC_REVERSE_SUBTRACT: ClassVar[int]
    GL_FUNC_SUBTRACT: ClassVar[int]
    GL_GENERATE_MIPMAP_HINT: ClassVar[int]
    GL_GEQUAL: ClassVar[int]
    GL_GREATER: ClassVar[int]
    GL_GREEN_BITS: ClassVar[int]
    GL_HIGH_FLOAT: ClassVar[int]
    GL_HIGH_INT: ClassVar[int]
    GL_IMPLEMENTATION_COLOR_READ_FORMAT: ClassVar[int]
    GL_IMPLEMENTATION_COLOR_READ_TYPE: ClassVar[int]
    GL_INCR: ClassVar[int]
    GL_INCR_WRAP: ClassVar[int]
    GL_INFO_LOG_LENGTH: ClassVar[int]
    GL_INT: ClassVar[int]
    GL_INT_VEC2: ClassVar[int]
    GL_INT_VEC3: ClassVar[int]
    GL_INT_VEC4: ClassVar[int]
    GL_INVALID_ENUM: ClassVar[int]
    GL_INVALID_FRAMEBUFFER_OPERATION: ClassVar[int]
    GL_INVALID_OPERATION: ClassVar[int]
    GL_INVALID_VALUE: ClassVar[int]
    GL_INVERT: ClassVar[int]
    GL_KEEP: ClassVar[int]
    GL_LEQUAL: ClassVar[int]
    GL_LESS: ClassVar[int]
    GL_LINEAR: ClassVar[int]
    GL_LINEAR_MIPMAP_LINEAR: ClassVar[int]
    GL_LINEAR_MIPMAP_NEAREST: ClassVar[int]
    GL_LINES: ClassVar[int]
    GL_LINE_LOOP: ClassVar[int]
    GL_LINE_STRIP: ClassVar[int]
    GL_LINE_WIDTH: ClassVar[int]
    GL_LINK_STATUS: ClassVar[int]
    GL_LOW_FLOAT: ClassVar[int]
    GL_LOW_INT: ClassVar[int]
    GL_LUMINANCE: ClassVar[int]
    GL_LUMINANCE_ALPHA: ClassVar[int]
    GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS: ClassVar[int]
    GL_MAX_CUBE_MAP_TEXTURE_SIZE: ClassVar[int]
    GL_MAX_FRAGMENT_UNIFORM_VECTORS: ClassVar[int]
    GL_MAX_RENDERBUFFER_SIZE: ClassVar[int]
    GL_MAX_TEXTURE_IMAGE_UNITS: ClassVar[int]
    GL_MAX_TEXTURE_SIZE: ClassVar[int]
    GL_MAX_VARYING_VECTORS: ClassVar[int]
    GL_MAX_VERTEX_ATTRIBS: ClassVar[int]
    GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS: ClassVar[int]
    GL_MAX_VERTEX_UNIFORM_VECTORS: ClassVar[int]
    GL_MAX_VIEWPORT_DIMS: ClassVar[int]
    GL_MEDIUM_FLOAT: ClassVar[int]
    GL_MEDIUM_INT: ClassVar[int]
    GL_MIRRORED_REPEAT: ClassVar[int]
    GL_NEAREST: ClassVar[int]
    GL_NEAREST_MIPMAP_LINEAR: ClassVar[int]
    GL_NEAREST_MIPMAP_NEAREST: ClassVar[int]
    GL_NEVER: ClassVar[int]
    GL_NICEST: ClassVar[int]
    GL_NONE: ClassVar[int]
    GL_NOTEQUAL: ClassVar[int]
    GL_NO_ERROR: ClassVar[int]
    GL_NUM_COMPRESSED_TEXTURE_FORMATS: ClassVar[int]
    GL_NUM_SHADER_BINARY_FORMATS: ClassVar[int]
    GL_ONE: ClassVar[int]
    GL_ONE_MINUS_CONSTANT_ALPHA: ClassVar[int]
    GL_ONE_MINUS_CONSTANT_COLOR: ClassVar[int]
    GL_ONE_MINUS_DST_ALPHA: ClassVar[int]
    GL_ONE_MINUS_DST_COLOR: ClassVar[int]
    GL_ONE_MINUS_SRC_ALPHA: ClassVar[int]
    GL_ONE_MINUS_SRC_COLOR: ClassVar[int]
    GL_OUT_OF_MEMORY: ClassVar[int]
    GL_PACK_ALIGNMENT: ClassVar[int]
    GL_POINTS: ClassVar[int]
    GL_POLYGON_OFFSET_FACTOR: ClassVar[int]
    GL_POLYGON_OFFSET_FILL: ClassVar[int]
    GL_POLYGON_OFFSET_UNITS: ClassVar[int]
    GL_RED_BITS: ClassVar[int]
    GL_RENDERBUFFER: ClassVar[int]
    GL_RENDERBUFFER_ALPHA_SIZE: ClassVar[int]
    GL_RENDERBUFFER_BINDING: ClassVar[int]
    GL_RENDERBUFFER_BLUE_SIZE: ClassVar[int]
    GL_RENDERBUFFER_DEPTH_SIZE: ClassVar[int]
    GL_RENDERBUFFER_GREEN_SIZE: ClassVar[int]
    GL_RENDERBUFFER_HEIGHT: ClassVar[int]
    GL_RENDERBUFFER_INTERNAL_FORMAT: ClassVar[int]
    GL_RENDERBUFFER_RED_SIZE: ClassVar[int]
    GL_RENDERBUFFER_STENCIL_SIZE: ClassVar[int]
    GL_RENDERBUFFER_WIDTH: ClassVar[int]
    GL_RENDERER: ClassVar[int]
    GL_REPEAT: ClassVar[int]
    GL_REPLACE: ClassVar[int]
    GL_RGB: ClassVar[int]
    GL_RGB565: ClassVar[int]
    GL_RGB5_A1: ClassVar[int]
    GL_RGBA: ClassVar[int]
    GL_RGBA4: ClassVar[int]
    GL_SAMPLER_2D: ClassVar[int]
    GL_SAMPLER_CUBE: ClassVar[int]
    GL_SAMPLES: ClassVar[int]
    GL_SAMPLE_ALPHA_TO_COVERAGE: ClassVar[int]
    GL_SAMPLE_BUFFERS: ClassVar[int]
    GL_SAMPLE_COVERAGE: ClassVar[int]
    GL_SAMPLE_COVERAGE_INVERT: ClassVar[int]
    GL_SAMPLE_COVERAGE_VALUE: ClassVar[int]
    GL_SCISSOR_BOX: ClassVar[int]
    GL_SCISSOR_TEST: ClassVar[int]
    GL_SHADER_BINARY_FORMATS: ClassVar[int]
    GL_SHADER_COMPILER: ClassVar[int]
    GL_SHADER_SOURCE_LENGTH: ClassVar[int]
    GL_SHADER_TYPE: ClassVar[int]
    GL_SHADING_LANGUAGE_VERSION: ClassVar[int]
    GL_SHORT: ClassVar[int]
    GL_SRC_ALPHA: ClassVar[int]
    GL_SRC_ALPHA_SATURATE: ClassVar[int]
    GL_SRC_COLOR: ClassVar[int]
    GL_STATIC_DRAW: ClassVar[int]
    GL_STENCIL_ATTACHMENT: ClassVar[int]
    GL_STENCIL_BACK_FAIL: ClassVar[int]
    GL_STENCIL_BACK_FUNC: ClassVar[int]
    GL_STENCIL_BACK_PASS_DEPTH_FAIL: ClassVar[int]
    GL_STENCIL_BACK_PASS_DEPTH_PASS: ClassVar[int]
    GL_STENCIL_BACK_REF: ClassVar[int]
    GL_STENCIL_BACK_VALUE_MASK: ClassVar[int]
    GL_STENCIL_BACK_WRITEMASK: ClassVar[int]
    GL_STENCIL_BITS: ClassVar[int]
    GL_STENCIL_BUFFER_BIT: ClassVar[int]
    GL_STENCIL_CLEAR_VALUE: ClassVar[int]
    GL_STENCIL_FAIL: ClassVar[int]
    GL_STENCIL_FUNC: ClassVar[int]
    GL_STENCIL_INDEX: ClassVar[int]
    GL_STENCIL_INDEX8: ClassVar[int]
    GL_STENCIL_PASS_DEPTH_FAIL: ClassVar[int]
    GL_STENCIL_PASS_DEPTH_PASS: ClassVar[int]
    GL_STENCIL_REF: ClassVar[int]
    GL_STENCIL_TEST: ClassVar[int]
    GL_STENCIL_VALUE_MASK: ClassVar[int]
    GL_STENCIL_WRITEMASK: ClassVar[int]
    GL_STREAM_DRAW: ClassVar[int]
    GL_SUBPIXEL_BITS: ClassVar[int]
    GL_TEXTURE: ClassVar[int]
    GL_TEXTURE0: ClassVar[int]
    GL_TEXTURE1: ClassVar[int]
    GL_TEXTURE10: ClassVar[int]
    GL_TEXTURE11: ClassVar[int]
    GL_TEXTURE12: ClassVar[int]
    GL_TEXTURE13: ClassVar[int]
    GL_TEXTURE14: ClassVar[int]
    GL_TEXTURE15: ClassVar[int]
    GL_TEXTURE16: ClassVar[int]
    GL_TEXTURE17: ClassVar[int]
    GL_TEXTURE18: ClassVar[int]
    GL_TEXTURE19: ClassVar[int]
    GL_TEXTURE2: ClassVar[int]
    GL_TEXTURE20: ClassVar[int]
    GL_TEXTURE21: ClassVar[int]
    GL_TEXTURE22: ClassVar[int]
    GL_TEXTURE23: ClassVar[int]
    GL_TEXTURE24: ClassVar[int]
    GL_TEXTURE25: ClassVar[int]
    GL_TEXTURE26: ClassVar[int]
    GL_TEXTURE27: ClassVar[int]
    GL_TEXTURE28: ClassVar[int]
    GL_TEXTURE29: ClassVar[int]
    GL_TEXTURE3: ClassVar[int]
    GL_TEXTURE30: ClassVar[int]
    GL_TEXTURE31: ClassVar[int]
    GL_TEXTURE4: ClassVar[int]
    GL_TEXTURE5: ClassVar[int]
    GL_TEXTURE6: ClassVar[int]
    GL_TEXTURE7: ClassVar[int]
    GL_TEXTURE8: ClassVar[int]
    GL_TEXTURE9: ClassVar[int]
    GL_TEXTURE_2D: ClassVar[int]
    GL_TEXTURE_BINDING_2D: ClassVar[int]
    GL_TEXTURE_BINDING_CUBE_MAP: ClassVar[int]
    GL_TEXTURE_CUBE_MAP: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_NEGATIVE_X: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_NEGATIVE_Y: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_NEGATIVE_Z: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_POSITIVE_X: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_POSITIVE_Y: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_POSITIVE_Z: ClassVar[int]
    GL_TEXTURE_MAG_FILTER: ClassVar[int]
    GL_TEXTURE_MIN_FILTER: ClassVar[int]
    GL_TEXTURE_WRAP_S: ClassVar[int]
    GL_TEXTURE_WRAP_T: ClassVar[int]
    GL_TRIANGLES: ClassVar[int]
    GL_TRIANGLE_FAN: ClassVar[int]
    GL_TRIANGLE_STRIP: ClassVar[int]
    GL_TRUE: ClassVar[int]
    GL_UNPACK_ALIGNMENT: ClassVar[int]
    GL_UNSIGNED_BYTE: ClassVar[int]
    GL_UNSIGNED_INT: ClassVar[int]
    GL_UNSIGNED_SHORT: ClassVar[int]
    GL_UNSIGNED_SHORT_4_4_4_4: ClassVar[int]
    GL_UNSIGNED_SHORT_5_5_5_1: ClassVar[int]
    GL_UNSIGNED_SHORT_5_6_5: ClassVar[int]
    GL_VALIDATE_STATUS: ClassVar[int]
    GL_VENDOR: ClassVar[int]
    GL_VERSION: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_ENABLED: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_NORMALIZED: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_POINTER: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_SIZE: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_STRIDE: ClassVar[int]
    GL_VERTEX_ATTRIB_ARRAY_TYPE: ClassVar[int]
    GL_VERTEX_SHADER: ClassVar[int]
    GL_VIEWPORT: ClassVar[int]
    GL_ZERO: ClassVar[int]
    @staticmethod
    def glDispatchComputeIndirect(p0: int) -> None: ...
    @staticmethod
    def glDrawArraysIndirect(p0: int, p1: int) -> None: ...
    @staticmethod
    def glDrawElementsIndirect(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glFramebufferParameteri(p0: int, p1: int, p2: int) -> None: ...
    @overload
    @staticmethod
    def glGenProgramPipelines(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGenProgramPipelines(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glGetBooleani_v(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetBooleani_v(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetFramebufferParameteriv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetFramebufferParameteriv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetMultisamplefv(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetMultisamplefv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetProgramInterfaceiv(p0: int, p1: int, p2: int, p3: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetProgramInterfaceiv(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @staticmethod
    def glGetProgramPipelineInfoLog(p0: int) -> str: ...
    @overload
    @staticmethod
    def glGetProgramPipelineiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetProgramPipelineiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @staticmethod
    def glGetProgramResourceIndex(p0: int, p1: int, p2: str) -> int: ...
    @staticmethod
    def glGetProgramResourceLocation(p0: int, p1: int, p2: str) -> int: ...
    @staticmethod
    def glGetProgramResourceName(p0: int, p1: int, p2: int) -> str: ...
    @overload
    @staticmethod
    def glGetProgramResourceiv(p0: int, p1: int, p2: int, p3: int, p4: Any, p5: int, p6: int, p7: Any, p8: int, p9: Any, p10: int) -> None: ...
    @overload
    @staticmethod
    def glGetProgramResourceiv(p0: int, p1: int, p2: int, p3: int, p4: IntBuffer, p5: int, p6: IntBuffer, p7: IntBuffer) -> None: ...
    @staticmethod
    def glActiveShaderProgram(p0: int, p1: int) -> None: ...
    @staticmethod
    def glBindImageTexture(p0: int, p1: int, p2: int, p3: bool, p4: int, p5: int, p6: int) -> None: ...
    @staticmethod
    def glBindProgramPipeline(p0: int) -> None: ...
    @staticmethod
    def glBindVertexBuffer(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glCreateShaderProgramv(p0: int, p1: Any) -> int: ...
    @overload
    @staticmethod
    def glDeleteProgramPipelines(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glDeleteProgramPipelines(p0: int, p1: Any, p2: int) -> None: ...
    @staticmethod
    def glDispatchCompute(p0: int, p1: int, p2: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexLevelParameteriv(p0: int, p1: int, p2: int, p3: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexLevelParameteriv(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @staticmethod
    def glIsProgramPipeline(p0: int) -> bool: ...
    @staticmethod
    def glMemoryBarrier(p0: int) -> None: ...
    @staticmethod
    def glMemoryBarrierByRegion(p0: int) -> None: ...
    @staticmethod
    def glProgramUniform1f(p0: int, p1: int, p2: float) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform1fv(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform1fv(p0: int, p1: int, p2: int, p3: FloatBuffer) -> None: ...
    @staticmethod
    def glProgramUniform1i(p0: int, p1: int, p2: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform1iv(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform1iv(p0: int, p1: int, p2: int, p3: IntBuffer) -> None: ...
    @staticmethod
    def glProgramUniform1ui(p0: int, p1: int, p2: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform1uiv(p0: int, p1: int, p2: int, p3: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform1uiv(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @staticmethod
    def glProgramUniform2f(p0: int, p1: int, p2: float, p3: float) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform2fv(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform2fv(p0: int, p1: int, p2: int, p3: FloatBuffer) -> None: ...
    @staticmethod
    def glProgramUniform2i(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform2iv(p0: int, p1: int, p2: int, p3: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform2iv(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @staticmethod
    def glProgramUniform2ui(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform2uiv(p0: int, p1: int, p2: int, p3: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform2uiv(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @staticmethod
    def glProgramUniform3f(p0: int, p1: int, p2: float, p3: float, p4: float) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform3fv(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform3fv(p0: int, p1: int, p2: int, p3: FloatBuffer) -> None: ...
    @staticmethod
    def glProgramUniform3i(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform3iv(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform3iv(p0: int, p1: int, p2: int, p3: IntBuffer) -> None: ...
    @staticmethod
    def glProgramUniform3ui(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform3uiv(p0: int, p1: int, p2: int, p3: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform3uiv(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @staticmethod
    def glProgramUniform4f(p0: int, p1: int, p2: float, p3: float, p4: float, p5: float) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform4fv(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform4fv(p0: int, p1: int, p2: int, p3: FloatBuffer) -> None: ...
    @staticmethod
    def glProgramUniform4i(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform4iv(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform4iv(p0: int, p1: int, p2: int, p3: IntBuffer) -> None: ...
    @staticmethod
    def glProgramUniform4ui(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform4uiv(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform4uiv(p0: int, p1: int, p2: int, p3: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix2fv(p0: int, p1: int, p2: int, p3: bool, p4: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix2fv(p0: int, p1: int, p2: int, p3: bool, p4: Any, p5: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix2x3fv(p0: int, p1: int, p2: int, p3: bool, p4: Any, p5: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix2x3fv(p0: int, p1: int, p2: int, p3: bool, p4: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix2x4fv(p0: int, p1: int, p2: int, p3: bool, p4: Any, p5: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix2x4fv(p0: int, p1: int, p2: int, p3: bool, p4: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix3fv(p0: int, p1: int, p2: int, p3: bool, p4: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix3fv(p0: int, p1: int, p2: int, p3: bool, p4: Any, p5: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix3x2fv(p0: int, p1: int, p2: int, p3: bool, p4: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix3x2fv(p0: int, p1: int, p2: int, p3: bool, p4: Any, p5: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix3x4fv(p0: int, p1: int, p2: int, p3: bool, p4: Any, p5: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix3x4fv(p0: int, p1: int, p2: int, p3: bool, p4: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix4fv(p0: int, p1: int, p2: int, p3: bool, p4: Any, p5: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix4fv(p0: int, p1: int, p2: int, p3: bool, p4: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix4x2fv(p0: int, p1: int, p2: int, p3: bool, p4: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix4x2fv(p0: int, p1: int, p2: int, p3: bool, p4: Any, p5: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix4x3fv(p0: int, p1: int, p2: int, p3: bool, p4: Any, p5: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix4x3fv(p0: int, p1: int, p2: int, p3: bool, p4: FloatBuffer) -> None: ...
    @staticmethod
    def glSampleMaski(p0: int, p1: int) -> None: ...
    @staticmethod
    def glTexStorage2DMultisample(p0: int, p1: int, p2: int, p3: int, p4: int, p5: bool) -> None: ...
    @staticmethod
    def glUseProgramStages(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glValidateProgramPipeline(p0: int) -> None: ...
    @staticmethod
    def glVertexAttribBinding(p0: int, p1: int) -> None: ...
    @staticmethod
    def glVertexAttribFormat(p0: int, p1: int, p2: int, p3: bool, p4: int) -> None: ...
    @staticmethod
    def glVertexAttribIFormat(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glVertexBindingDivisor(p0: int, p1: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexLevelParameterfv(p0: int, p1: int, p2: int, p3: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexLevelParameterfv(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...

from typing import Any, ClassVar, overload
from java.nio.Buffer import Buffer

class ETC1:
    DECODED_BLOCK_SIZE: ClassVar[int]
    ENCODED_BLOCK_SIZE: ClassVar[int]
    ETC1_RGB8_OES: ClassVar[int]
    ETC_PKM_HEADER_SIZE: ClassVar[int]
    def __init__(self) -> None: ...
    @staticmethod
    def decodeImage(p0: Buffer, p1: Buffer, p2: int, p3: int, p4: int, p5: int) -> None: ...
    @staticmethod
    def encodeImage(p0: Buffer, p1: int, p2: int, p3: int, p4: int, p5: Buffer) -> None: ...
    @staticmethod
    def formatHeader(p0: Buffer, p1: int, p2: int) -> None: ...
    @staticmethod
    def getEncodedDataSize(p0: int, p1: int) -> int: ...
    @staticmethod
    def encodeBlock(p0: Buffer, p1: int, p2: Buffer) -> None: ...
    @staticmethod
    def decodeBlock(p0: Buffer, p1: Buffer) -> None: ...
    @staticmethod
    def getHeight(p0: Buffer) -> int: ...
    @staticmethod
    def getWidth(p0: Buffer) -> int: ...
    @staticmethod
    def isValid(p0: Buffer) -> bool: ...

