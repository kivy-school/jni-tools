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
    def glDispatchCompute(p0: int, p1: int, p2: int) -> None: ...
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
    def glGetFramebufferParameteriv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetFramebufferParameteriv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetProgramInterfaceiv(p0: int, p1: int, p2: int, p3: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetProgramInterfaceiv(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @staticmethod
    def glGetProgramResourceIndex(p0: int, p1: int, p2: str) -> int: ...
    @staticmethod
    def glGetProgramResourceName(p0: int, p1: int, p2: int) -> str: ...
    @overload
    @staticmethod
    def glGetProgramResourceiv(p0: int, p1: int, p2: int, p3: int, p4: IntBuffer, p5: int, p6: IntBuffer, p7: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetProgramResourceiv(p0: int, p1: int, p2: int, p3: int, p4: Any, p5: int, p6: int, p7: Any, p8: int, p9: Any, p10: int) -> None: ...
    @staticmethod
    def glGetProgramResourceLocation(p0: int, p1: int, p2: str) -> int: ...
    @staticmethod
    def glUseProgramStages(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glActiveShaderProgram(p0: int, p1: int) -> None: ...
    @staticmethod
    def glCreateShaderProgramv(p0: int, p1: Any) -> int: ...
    @staticmethod
    def glBindProgramPipeline(p0: int) -> None: ...
    @overload
    @staticmethod
    def glDeleteProgramPipelines(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glDeleteProgramPipelines(p0: int, p1: Any, p2: int) -> None: ...
    @overload
    @staticmethod
    def glGenProgramPipelines(p0: int, p1: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGenProgramPipelines(p0: int, p1: Any, p2: int) -> None: ...
    @staticmethod
    def glIsProgramPipeline(p0: int) -> bool: ...
    @overload
    @staticmethod
    def glGetProgramPipelineiv(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetProgramPipelineiv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def glProgramUniform1i(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glProgramUniform2i(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glProgramUniform3i(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @staticmethod
    def glProgramUniform4i(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int) -> None: ...
    @staticmethod
    def glProgramUniform1ui(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glProgramUniform2ui(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glProgramUniform3ui(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @staticmethod
    def glProgramUniform4ui(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int) -> None: ...
    @staticmethod
    def glProgramUniform1f(p0: int, p1: int, p2: float) -> None: ...
    @staticmethod
    def glProgramUniform2f(p0: int, p1: int, p2: float, p3: float) -> None: ...
    @staticmethod
    def glProgramUniform3f(p0: int, p1: int, p2: float, p3: float, p4: float) -> None: ...
    @staticmethod
    def glProgramUniform4f(p0: int, p1: int, p2: float, p3: float, p4: float, p5: float) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform1iv(p0: int, p1: int, p2: int, p3: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform1iv(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform2iv(p0: int, p1: int, p2: int, p3: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform2iv(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform3iv(p0: int, p1: int, p2: int, p3: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform3iv(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform4iv(p0: int, p1: int, p2: int, p3: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform4iv(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform1uiv(p0: int, p1: int, p2: int, p3: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform1uiv(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform2uiv(p0: int, p1: int, p2: int, p3: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform2uiv(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform3uiv(p0: int, p1: int, p2: int, p3: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform3uiv(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform4uiv(p0: int, p1: int, p2: int, p3: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform4uiv(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform1fv(p0: int, p1: int, p2: int, p3: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform1fv(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform2fv(p0: int, p1: int, p2: int, p3: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform2fv(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform3fv(p0: int, p1: int, p2: int, p3: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform3fv(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform4fv(p0: int, p1: int, p2: int, p3: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniform4fv(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix2fv(p0: int, p1: int, p2: int, p3: bool, p4: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix2fv(p0: int, p1: int, p2: int, p3: bool, p4: Any, p5: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix3fv(p0: int, p1: int, p2: int, p3: bool, p4: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix3fv(p0: int, p1: int, p2: int, p3: bool, p4: Any, p5: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix4fv(p0: int, p1: int, p2: int, p3: bool, p4: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix4fv(p0: int, p1: int, p2: int, p3: bool, p4: Any, p5: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix2x3fv(p0: int, p1: int, p2: int, p3: bool, p4: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix2x3fv(p0: int, p1: int, p2: int, p3: bool, p4: Any, p5: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix3x2fv(p0: int, p1: int, p2: int, p3: bool, p4: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix3x2fv(p0: int, p1: int, p2: int, p3: bool, p4: Any, p5: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix2x4fv(p0: int, p1: int, p2: int, p3: bool, p4: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix2x4fv(p0: int, p1: int, p2: int, p3: bool, p4: Any, p5: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix4x2fv(p0: int, p1: int, p2: int, p3: bool, p4: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix4x2fv(p0: int, p1: int, p2: int, p3: bool, p4: Any, p5: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix3x4fv(p0: int, p1: int, p2: int, p3: bool, p4: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix3x4fv(p0: int, p1: int, p2: int, p3: bool, p4: Any, p5: int) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix4x3fv(p0: int, p1: int, p2: int, p3: bool, p4: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glProgramUniformMatrix4x3fv(p0: int, p1: int, p2: int, p3: bool, p4: Any, p5: int) -> None: ...
    @staticmethod
    def glValidateProgramPipeline(p0: int) -> None: ...
    @staticmethod
    def glGetProgramPipelineInfoLog(p0: int) -> str: ...
    @staticmethod
    def glBindImageTexture(p0: int, p1: int, p2: int, p3: bool, p4: int, p5: int, p6: int) -> None: ...
    @overload
    @staticmethod
    def glGetBooleani_v(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetBooleani_v(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def glMemoryBarrier(p0: int) -> None: ...
    @staticmethod
    def glMemoryBarrierByRegion(p0: int) -> None: ...
    @staticmethod
    def glTexStorage2DMultisample(p0: int, p1: int, p2: int, p3: int, p4: int, p5: bool) -> None: ...
    @overload
    @staticmethod
    def glGetMultisamplefv(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetMultisamplefv(p0: int, p1: int, p2: FloatBuffer) -> None: ...
    @staticmethod
    def glSampleMaski(p0: int, p1: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexLevelParameteriv(p0: int, p1: int, p2: int, p3: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexLevelParameteriv(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexLevelParameterfv(p0: int, p1: int, p2: int, p3: FloatBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexLevelParameterfv(p0: int, p1: int, p2: int, p3: Any, p4: int) -> None: ...
    @staticmethod
    def glBindVertexBuffer(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glVertexAttribFormat(p0: int, p1: int, p2: int, p3: bool, p4: int) -> None: ...
    @staticmethod
    def glVertexAttribIFormat(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glVertexAttribBinding(p0: int, p1: int) -> None: ...
    @staticmethod
    def glVertexBindingDivisor(p0: int, p1: int) -> None: ...
